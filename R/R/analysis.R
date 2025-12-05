#' Interrater Reliability Analysis Functions
#'
#' Functions for analyzing interrater reliability in medevac decision vignettes.
#'
#' @name analysis
#' @docType package
NULL

#' Calculate percentage agreement for a given question
#'
#' @param data Data frame with columns: physician_id, question, decision
#' @param question_id Question number (1-20). If NULL, calculates overall.
#' @return Percentage agreement (0-1)
#' @export
calculate_percentage_agreement <- function(data, question_id = NULL) {
  if (!is.null(question_id)) {
    data <- data[data$question == question_id, ]
  }
  
  if (nrow(data) == 0) {
    return(NA)
  }
  
  # Get all unique physician pairs
  physicians <- unique(data$physician_id)
  n_physicians <- length(physicians)
  
  if (n_physicians < 2) {
    return(NA)
  }
  
  # Count agreements for each question
  agreements <- 0
  total_pairs <- 0
  
  for (q in unique(data$question)) {
    q_data <- data[data$question == q, ]
    decisions <- setNames(q_data$decision, q_data$physician_id)
    
    # Compare all pairs
    for (i in 1:(n_physicians - 1)) {
      for (j in (i + 1):n_physicians) {
        p1 <- physicians[i]
        p2 <- physicians[j]
        
        if (p1 %in% names(decisions) && p2 %in% names(decisions)) {
          total_pairs <- total_pairs + 1
          if (decisions[[as.character(p1)]] == decisions[[as.character(p2)]]) {
            agreements <- agreements + 1
          }
        }
      }
    }
  }
  
  if (total_pairs == 0) {
    return(NA)
  }
  
  return(agreements / total_pairs)
}

#' Calculate Fleiss' Kappa for multiple raters
#'
#' @param data Data frame with columns: physician_id, question, decision
#' @param question_id Question number (1-20)
#' @return Fleiss' Kappa value
#' @export
calculate_fleiss_kappa <- function(data, question_id) {
  q_data <- data[data$question == question_id, ]
  
  if (nrow(q_data) == 0) {
    return(NA)
  }
  
  decisions <- unique(q_data$decision)
  n_categories <- length(decisions)
  n_raters <- length(unique(q_data$physician_id))
  
  if (n_categories < 2 || n_raters < 2) {
    return(NA)
  }
  
  # Create rating matrix
  rating_matrix <- matrix(0, nrow = n_raters, ncol = n_categories)
  
  for (i in seq_len(nrow(q_data))) {
    decision <- q_data$decision[i]
    cat_idx <- which(decisions == decision)
    rating_matrix[i, cat_idx] <- 1
  }
  
  # Calculate Fleiss' Kappa using irr package if available
  if (requireNamespace("irr", quietly = TRUE)) {
    # Reshape to format irr expects (each row is a subject, columns are raters)
    # For our data, each question is a subject
    kappa_result <- tryCatch({
      # Convert to irr format: matrix where rows are subjects, cols are raters
      irr_format <- matrix(NA, nrow = 1, ncol = n_raters)
      for (i in seq_len(n_raters)) {
        decision_idx <- which(rating_matrix[i, ] == 1)
        if (length(decision_idx) > 0) {
          irr_format[1, i] <- decision_idx
        }
      }
      irr::kappam.fleiss(irr_format)
    }, error = function(e) {
      return(list(value = NA))
    })
    
    if (!is.null(kappa_result$value)) {
      return(kappa_result$value)
    }
  }
  
  # Fallback: manual calculation
  P_j <- colSums(rating_matrix) / n_raters
  P_i <- rowSums(rating_matrix^2) / (n_categories - 1)
  P_bar <- mean(P_i)
  P_e <- sum(P_j^2)
  
  if (P_e == 1) {
    return(NA)  # Perfect chance agreement
  }
  
  kappa <- (P_bar - P_e) / (1 - P_e)
  return(kappa)
}

#' Calculate agreement metrics by vignette class
#'
#' @param data Data frame with columns: physician_id, question, decision, vignette_class
#' @return Data frame with agreement metrics by class
#' @export
calculate_agreement_by_class <- function(data) {
  results <- list()
  
  for (v_class in unique(data$vignette_class)) {
    class_data <- data[data$vignette_class == v_class, ]
    questions <- unique(class_data$question)
    
    # Calculate percentage agreement for each question
    agreements <- sapply(questions, function(q) {
      q_data <- class_data[class_data$question == q, ]
      calculate_percentage_agreement(q_data, question_id = NULL)
    })
    
    # Calculate Fleiss' Kappa for each question
    kappas <- sapply(questions, function(q) {
      calculate_fleiss_kappa(class_data, q)
    })
    
    results[[length(results) + 1]] <- data.frame(
      vignette_class = v_class,
      n_questions = length(questions),
      mean_percentage_agreement = mean(agreements, na.rm = TRUE),
      mean_fleiss_kappa = mean(kappas, na.rm = TRUE),
      stringsAsFactors = FALSE
    )
  }
  
  return(do.call(rbind, results))
}

#' Calculate question-level metrics
#'
#' @param data Data frame with columns: physician_id, question, decision, vignette_class
#' @return Data frame with metrics for each question
#' @export
calculate_question_level_metrics <- function(data) {
  results <- list()
  
  for (q in sort(unique(data$question))) {
    q_data <- data[data$question == q, ]
    
    # Percentage agreement
    pa <- calculate_percentage_agreement(q_data, question_id = NULL)
    
    # Fleiss' Kappa
    fk <- calculate_fleiss_kappa(data, q)
    
    # Decision distribution
    decision_counts <- table(q_data$decision)
    
    # Get vignette info
    vignette_info <- q_data[1, ]
    
    results[[length(results) + 1]] <- data.frame(
      question = q,
      question_type = vignette_info$question_type,
      vignette_class = vignette_info$vignette_class,
      n_physicians = length(unique(q_data$physician_id)),
      percentage_agreement = pa,
      fleiss_kappa = fk,
      decision_medevac = as.numeric(ifelse(is.na(decision_counts["Medevac"]), 0, decision_counts["Medevac"])),
      decision_commercial = as.numeric(ifelse(is.na(decision_counts["Commercial"]), 0, decision_counts["Commercial"])),
      decision_remain = as.numeric(ifelse(is.na(decision_counts["Remain"]), 0, decision_counts["Remain"])),
      stringsAsFactors = FALSE
    )
  }
  
  return(do.call(rbind, results))
}

#' Analyze confidence ratings
#'
#' @param data Data frame with confidence column
#' @return List with confidence by decision and by class
#' @export
analyze_confidence <- function(data) {
  # Confidence by decision
  conf_by_decision <- aggregate(
    confidence ~ decision,
    data = data,
    FUN = function(x) c(mean = mean(x, na.rm = TRUE), sd = sd(x, na.rm = TRUE), n = length(x))
  )
  
  # Confidence by vignette class
  conf_by_class <- aggregate(
    confidence ~ vignette_class,
    data = data,
    FUN = function(x) c(mean = mean(x, na.rm = TRUE), sd = sd(x, na.rm = TRUE), n = length(x))
  )
  
  return(list(
    by_decision = conf_by_decision,
    by_class = conf_by_class
  ))
}

