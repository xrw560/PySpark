import pandas as pd

"""预处理"""
loans_2007 = pd.read_csv("loans_2007.csv")
loans_2007.drop_duplicates()
# print(loans_2007.iloc[0])
print(loans_2007.shape[1])

loans_2007 = loans_2007.drop(
    ["id", "member_id", "funded_amnt", "funded_amnt_inv", "grade", "sub_grade", "emp_title", "issue_d"], axis=1)

loans_2007 = loans_2007.drop(
    ["zip_code", "out_prncp", "out_prncp_inv", "total_pymnt", "total_pymnt_inv", "total_rec_prncp"], axis=1)

loans_2007 = loans_2007.drop(
    ["total_rec_int", "total_rec_late_fee", "recoveries", "collection_recovery_fee", "last_pymnt_d", "last_pymnt_amnt"],
    axis=1)
# print(loans_2007.iloc[0])
print(loans_2007.shape[1])

# print(loans_2007['loan_status'].value_counts()) #贷款状态

loans_2007 = loans_2007[(loans_2007['loan_status'] == "Fully Paid") | (loans_2007['loan_status'] == "Charged Off")]

status_replace = {
    "loan_status": {
        "Fully Paid": 1,
        "Charged Off": 0,
    }
}

loans_2007 = loans_2007.replace(status_replace)

# let's look for any columns that contain only one unique value and remove them

orig_columns = loans_2007.columns
drop_columns = []
for col in orig_columns:
    col_series = loans_2007[col].dropna().unique()  # 唯一的属性
    if len(col_series) == 1:
        drop_columns.append(col)
loans_2007 = loans_2007.drop(drop_columns, axis=1)  #
print(drop_columns)
print(loans_2007.shape)
loans_2007.to_csv('filtered_loans_2007.csv', index=False)
