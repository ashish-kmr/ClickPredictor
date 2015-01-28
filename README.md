# ClickPredictor

Commands:

python process_data_train.py < train.csv > train_processed.csv      
Converts data to the input format of vw


vw -d train_processed.csv --cache_file cache_train -f r_temp     
trains the learner and save it in r_temp


python process_data_test.py < test.csv > test_processed.csv      
Converts data to the input format of vw


vw -t -d test_processed.csv --cache_file cache_test -i r_temp -p p_out.csv    
Generates output on test data


python submit_format.py > submission1.csv                        
Converts to submission format
