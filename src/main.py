import mlflow 
import argparse



def main(training=True):
    with mlflow.start_run() as run:
      
        print("###### Training ######")
        mlflow.run(".", "stage_01", use_conda=False)
        mlflow.run(".", "stage_02", use_conda=False)
        mlflow.run(".", "stage_03", use_conda=False)
        mlflow.run(".", "stage_04", use_conda=False)
        #else:
            #print("###### Predicting ######")
            #mlflow.run(".", "stage_01", use_conda=False)
            #mlflow.run(".", "stage_03", use_conda=False)


if __name__ == '__main__':
    main()