from src.textSummarizer.pipeline.data_ingestion import DataIngestionTrainingPipeline
# from src.textSummarizer.pipeline.data_validation import DataValidationTrainingPipeline
# from src.textSummarizer.pipeline.data_transformation import DataTransformationTrainingPipeline
# from src.textSummarizer.pipeline.model_trainer import ModelTrainerTrainingPipeline
# from src.textSummarizer.pipeline.model_evaluation import ModelEvaluationTrainingPipeline

from textSummarizer.logging import logger


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e