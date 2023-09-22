# %%
import pandas as pd
import numpy as np

# %%
papers=pd.read_excel("myworks.xlsx",sheet_name="发表论文")

for i in papers.index:
	year=papers.loc[i,"papers"].split(". ")[0].split(" 20")[-1].strip("abcdefghijklmn")
	papers.loc[i,'Year']="20"+year

papers=papers.sort_values(by="Year",ascending=False)
papers.to_csv("publications.csv")

# %%
projects=pd.read_excel("myworks.xlsx",sheet_name="承担项目").fillna(0)

projects=projects.sort_values(by=["开始年份","类型"],ascending=False)
projects.to_csv("projects.csv")

# %%
under_courses=pd.read_excel("myworks.xlsx",sheet_name="教授本科课程").fillna(0)
under_courses=under_courses.sort_values(by=["学年起始","学期"],ascending=False)
under_courses.to_csv("under_courses.csv")

# %%
rewards=pd.read_excel("myworks.xlsx",sheet_name="获得奖项")
rewards=rewards.sort_values(by=["年","月"],ascending=False)
rewards.to_csv("rewards.csv")

under_rewards=pd.read_excel("myworks.xlsx",sheet_name="本科生获得奖励")
under_rewards=under_rewards.sort_values(by=["年"],ascending=False)
under_rewards.to_csv("under_rewards.csv")

grad_rewards=pd.read_excel("myworks.xlsx",sheet_name="研究生获得奖励")
grad_rewards=grad_rewards.sort_values(by=["年"],ascending=False)
grad_rewards.to_csv("grad_rewards.csv")

under_thesis=pd.read_excel("myworks.xlsx",sheet_name="指导本科生毕业论文")
under_thesis=under_thesis.sort_values(by=["年"],ascending=False)
under_thesis.to_csv("under_thesis.csv")

grad_thesis=pd.read_excel("myworks.xlsx",sheet_name="指导研究生毕业论文")
grad_thesis=grad_thesis.sort_values(by=["年"],ascending=False)
grad_thesis.to_csv("grad_thesis.csv")