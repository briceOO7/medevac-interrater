#!/usr/bin/env Rscript
# Main R analysis script for medevac interrater reliability study
#
# This script loads processed data from Python and performs all statistical analyses.

# Setup - find project root
# Try to find project root by looking for common markers
find_project_root <- function() {
  current <- normalizePath(getwd())
  max_depth <- 10
  depth <- 0
  
  while (depth < max_depth) {
    if (file.exists(file.path(current, "data", "processed")) ||
        file.exists(file.path(current, "R", "R", "analysis.R"))) {
      return(current)
    }
    parent <- dirname(current)
    if (parent == current) break
    current <- parent
    depth <- depth + 1
  }
  
  # Fallback: assume we're in scripts/r/
  return(normalizePath(file.path(getwd(), "..", "..")))
}

project_root <- find_project_root()

# Source analysis functions
source(file.path(project_root, "R", "R", "analysis.R"))

# Paths
data_dir <- file.path(project_root, "data", "processed")
output_dir <- file.path(project_root, "output")
dir.create(output_dir, showWarnings = FALSE)

# Load processed data
cat(strrep("=", 80), "\n")
cat("MEDEVAC INTERRATER RELIABILITY ANALYSIS - R\n")
cat(strrep("=", 80), "\n\n")

data_file <- file.path(data_dir, "survey_data_processed.csv")
if (!file.exists(data_file)) {
  stop("Processed data file not found. Please run Python data processing first.")
}

cat("📥 Loading processed data...\n")
data <- read.csv(data_file, stringsAsFactors = FALSE)
cat(sprintf("   ✓ Loaded %d rows\n", nrow(data)))
cat(sprintf("   ✓ %d unique physicians\n", length(unique(data$physician_id))))
cat(sprintf("   ✓ %d unique questions\n", length(unique(data$question))))
cat("\n")

# Overall percentage agreement
cat(strrep("=", 80), "\n")
cat("OVERALL AGREEMENT\n")
cat(strrep("=", 80), "\n")
overall_pa <- calculate_percentage_agreement(data, question_id = NULL)
cat(sprintf("Overall Percentage Agreement: %.3f (%.1f%%)\n", overall_pa, overall_pa * 100))
cat("\n")

# Question-level metrics
cat(strrep("=", 80), "\n")
cat("QUESTION-LEVEL METRICS\n")
cat(strrep("=", 80), "\n")
question_metrics <- calculate_question_level_metrics(data)
print(question_metrics)
write.csv(question_metrics, 
          file.path(output_dir, "question_level_metrics.csv"), 
          row.names = FALSE)
cat("\n💾 Saved to: question_level_metrics.csv\n\n")

# Agreement by vignette class
cat(strrep("=", 80), "\n")
cat("AGREEMENT BY VIGNETTE CLASS\n")
cat(strrep("=", 80), "\n")
class_metrics <- calculate_agreement_by_class(data)
print(class_metrics)
write.csv(class_metrics, 
          file.path(output_dir, "class_level_metrics.csv"), 
          row.names = FALSE)
cat("\n💾 Saved to: class_level_metrics.csv\n\n")

# Confidence analysis
cat(strrep("=", 80), "\n")
cat("CONFIDENCE ANALYSIS\n")
cat(strrep("=", 80), "\n")
conf_analysis <- analyze_confidence(data)
cat("\nConfidence by Decision:\n")
print(conf_analysis$by_decision)
write.csv(conf_analysis$by_decision, 
          file.path(output_dir, "confidence_by_decision.csv"), 
          row.names = FALSE)

cat("\nConfidence by Vignette Class:\n")
print(conf_analysis$by_class)
write.csv(conf_analysis$by_class, 
          file.path(output_dir, "confidence_by_class.csv"), 
          row.names = FALSE)
cat("\n💾 Saved confidence analyses\n\n")

# Summary statistics
cat(strrep("=", 80), "\n")
cat("SUMMARY STATISTICS\n")
cat(strrep("=", 80), "\n")
cat(sprintf("Mean Percentage Agreement: %.3f\n", mean(question_metrics$percentage_agreement, na.rm = TRUE)))
cat(sprintf("Mean Fleiss' Kappa: %.3f\n", mean(question_metrics$fleiss_kappa, na.rm = TRUE)))
cat(sprintf("Mean Confidence: %.2f\n", mean(data$confidence, na.rm = TRUE)))
cat(sprintf("SD Confidence: %.2f\n", sd(data$confidence, na.rm = TRUE)))
cat("\n")

# Decision distribution
cat("Decision Distribution:\n")
decision_dist <- table(data$decision)
for (decision in names(decision_dist)) {
  count <- decision_dist[[decision]]
  pct <- (count / nrow(data)) * 100
  cat(sprintf("  %s: %d (%.1f%%)\n", decision, count, pct))
}
cat("\n")

cat(strrep("=", 80), "\n")
cat("✅ Analysis complete!\n")
cat(strrep("=", 80), "\n")
cat(sprintf("\nAll results saved to: %s\n", output_dir))
cat("\n")

