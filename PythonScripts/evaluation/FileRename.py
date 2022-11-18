import pandas as pd
import shutil
from openpyxl import load_workbook

start = 0
end = 19

SampleFileName = "Evaluation Sheet"
trainee_file = pd.read_excel("traineesDetails.xlsx")
trainee_file["GIT repository link"].fillna("No link", inplace=True)
trainees = trainee_file[start:end]
print(trainees.columns)
# trainee_names = list(trainee_file["User Name"])
# trainees = dict(zip(trainees['User Name'], trainees['GIT repository link']))


def generate_file(row):
    name = row['User Name']
    link = row["GIT repository link"]
    email = row["Email"]
    file_name = f"{SampleFileName} - {name}.xlsx"
    shutil.copyfile(f"{SampleFileName}.xlsx", file_name)

    # load excel file
    workbook = load_workbook(filename=file_name)

    # open workbook
    sheet = workbook.active

    # modify the desired cell

    sheet["A2"] = name
    sheet["B2"] = email
    sheet["C2"] = link

    # save the file
    workbook.save(filename=file_name)


trainees.apply(generate_file, axis=1)