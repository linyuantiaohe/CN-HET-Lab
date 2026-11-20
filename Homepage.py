import streamlit as st
import pandas as pd
import numpy as np
import os
from PIL import Image

st.set_page_config(
    page_title="CN-HET Lab",
    page_icon="😎",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "Work hard!"
    }
)

os.system('python initial.py')

#st.image(Image.open('photos/logo.png'))
st.header("碳中和-氢电交通耦合系统实验室")
st.sidebar.markdown("诚招勤奋、好学、踏实的研究生, 急需有编程背景的同学。")
st.sidebar.markdown("E-mail: wangge@ncepu.edu.cn")
st.sidebar.markdown("地址: 北京市昌平区北农路2号")
st.sidebar.map(pd.DataFrame(pd.Series([40.088243727163956,116.30600799534605],index=['lat', 'lon']),columns=['Ncepu']).T)

col1,col2=st.columns([9,1])
col1.subheader("王歌 博士")
col1.markdown("**华北电力大学 经济与管理学院 副教授, 硕士生导师**")

myphoto = Image.open('photos/homepage.jpeg')
col2.image(myphoto)


page1, page2, page3, page4 =st.tabs(["个人简历","科研工作","研究生培养","本科生培养"])

#-----------------page1
page1.subheader("个人简历")

page1.markdown("华北电力大学经济与管理学院副教授，硕士生导师，院长助理，碳中和管理教研室主任。于南京大学获得天文学学士学位，于中国石油大学（北京）硕博连读获得管理学博士学位，于美国劳伦斯伯克利国家实验室博士联培。主持国家自然科学基金、北京社科基金、河北省自科基金等科研项目10余项，发表论文40余篇，获得各级科研教学奖励10余项。")

p1tab1, p1tab2, p1tab3 =page1.tabs(["个人经历","研究兴趣","招生需求"])
#tab1.markdown('**工作和教育经历**')

p1tab1.markdown("[1] 2024-     华北电力大学 经济与管理学院 副教授")
p1tab1.markdown("[2] 2019-2023 华北电力大学 经济与管理学院 讲师")
p1tab1.markdown("[3] 2014-2019 中国石油大学（北京）中国能源战略研究院/经济管理学院 硕博连读")
p1tab1.markdown("[4] 2018-2019 美国加州大学伯克利分校 劳伦斯伯克利国家实验室 联合培养")
p1tab1.markdown("[5] 2009-2013 南京大学 天文与空间科学学院 本科")

#tab2.markdown('**研究兴趣**')

p1tab2.markdown("- 绿氢氨醇技术经济分析与市场、政策研究")
p1tab2.markdown("- 算电协同系统模型")
p1tab2.markdown("- 电力市场、碳市场")

#tab3.markdown('**招生方向**')

p1tab3.markdown("- 具有经济学、能源、环境、计算机相关背景")
p1tab3.markdown("- 对能源环境经济和管理具有兴趣")
p1tab3.markdown("- 具备英文论文阅读能力")

#-----------------page2
page2.subheader("科研工作")

papers=pd.read_csv("publications.csv")
books=pd.read_csv("books.csv")
projects=pd.read_csv("projects.csv")
rewards=pd.read_csv("rewards.csv")
software=pd.read_csv("software.csv")
presentations=pd.read_csv("presentation.csv")
media=pd.read_csv("media.csv")

page2.markdown("- 累计发表论文%d篇,出版著作%d部"%(len(papers),len(books)))
page2.markdown("- 主持科研项目%d项, 累计承担经费:  %.1f万元"%(len(projects[projects["参与情况"]=="主持"]),projects["金额"].sum()))
page2.markdown("- 获得各类奖项%d项"%len(rewards))

p2tab1,p2tab5, p2tab2, p2tab3, p2tab4, p2tab6, p2tab7 =page2.tabs(["发表论文","出版著作","承担项目","获得奖项","专利和软件著作权","会议发表","媒体报道"])

item=0
year=papers.iloc[0].loc["Year"]
p2tab1.markdown("**%d**"%year)
for i in papers.index:
	if papers.loc[i,'Year']<year:
		year=papers.loc[i,'Year']
		p2tab1.markdown("**%d**"%year)
	p2tab1.markdown("[%d] %s"%(item+1,papers.loc[i,'papers']))
	item+=1

for i in books.index:
	p2tab5.markdown("[%d] %s, %s, %d, %s. **%s**"%(i+1,books.loc[i,'作者'],books.loc[i,'著作标题'],books.loc[i,'年份'],books.loc[i,'出版社'],books.loc[i,'著作类型']))

for i in projects.index:
	if projects.loc[i,"参与情况"]=="主持":
		p2tab2.markdown("[%d] **%s**, %s, %s, %.1f 万元。 %d - %d, %s."%(i+1,projects.loc[i,"项目类型"].strip(" "),projects.loc[i,"项目标题"].strip(" "),projects.loc[i,"参与情况"],projects.loc[i,"金额"],projects.loc[i,"开始年份"],projects.loc[i,"结束年份"],projects.loc[i,"在研情况"]))
	else:
		p2tab2.markdown("[%d] **%s**, %s, %s。%d - %d, %s."%(i+1,projects.loc[i,"项目类型"].strip(" "),projects.loc[i,"项目标题"].strip(" "),projects.loc[i,"参与情况"],projects.loc[i,"开始年份"],projects.loc[i,"结束年份"],projects.loc[i,"在研情况"]))

for i in rewards.index:
	if rewards.loc[i,'类型'] != "其它":
		p2tab3.markdown("[%d] %s %s. 排名第%d. %d年."%(i+1,rewards.loc[i,'奖项'],rewards.loc[i,'等级'],rewards.loc[i,'排名'],rewards.loc[i,'年']))
	else:
		p2tab3.markdown("[%d] %s. %d年."%(i+1,rewards.loc[i,'奖项'],rewards.loc[i,'年']))

for i in software.index:
	p2tab4.markdown("[%d] %s.(**%s**). %d年."%(i+1,software.loc[i,'题目'],software.loc[i,'类型'],software.loc[i,'年份']))

for i in presentations.index:
	p2tab6.markdown("[%d] %s. %s, **%s**. %s, %d年."%(i+1,presentations.loc[i,'题目'],presentations.loc[i,'会议名称'],presentations.loc[i,'发表类型'],presentations.loc[i,'地点'],presentations.loc[i,'年份']))

for i in media.index:
	p2tab7.markdown("[%d] %s. %s, %s. %d年."%(i+1,media.loc[i,'题目'],media.loc[i,'媒体'],media.loc[i,'类型'],media.loc[i,'年份']))
#-----------------page3

page3.subheader('研究生培养')

grad_thesis=pd.read_csv("grad_thesis.csv")

page3.markdown("组内有在读全日制硕士研究生12人，非全日制硕士研究生17人，已毕业硕士研究生%d人。"%(len(grad_thesis)))

p3tab1, p3tab2, p3tab3 =page3.tabs(["在读同学","指导毕业论文","指导获奖"])

##------------------------page3-1
majors=["工业工程与管理","物流工程与管理","工商管理"]
p3tab1.subheader('在读-2026级')

p3tab1.markdown('(%s 全日制) **赵婉悦.**'%majors[2])
p3tab1.markdown('(%s 全日制) **范梦颖，鲍敏敏.**'%majors[0])
p3tab1.markdown('(%s 非全日制) **陈琪, 阚启明, 马腾.**'%majors[2])
p3tab1.markdown('(%s 非全日制) **郑博焘，李响，刘佳梁，王洋洋.**'%majors[0])

p3tab1.subheader('在读-2025级')

p3tab1.markdown('(%s 全日制) **刘源, 申宇婷.**'%majors[2])
p3tab1.markdown('(%s 全日制) **白静茹, 吕乐文, 伏宇晟.**'%majors[0])
p3tab1.markdown('(%s 非全日制) **李凯烨, 杜哲, 杨盛, 马子辰, 乔艳婷.**'%majors[2])
p3tab1.markdown('(%s 非全日制) **陈俊潼.**'%majors[1])

p3tab1.subheader('在读-2024级')

p3tab1.markdown('(%s 全日制) **孔思婕.**'%majors[2])
p3tab1.markdown('(%s 全日制) **宫驰, 王菁, 万雨.**'%majors[0])
p3tab1.markdown('(%s 非全日制) **周剑剑, 王一民, 都奎影.**'%majors[2])
p3tab1.markdown('(%s 非全日制) **史丽航.**'%majors[0])
p3tab1.text('\n')
##------------------------page3-2
p3tab2.subheader('毕业论文')

for i in grad_thesis.index:
	p3tab2.markdown("- %d届, %s. %s."%(grad_thesis.loc[i,'年'],grad_thesis.loc[i,'姓名'],grad_thesis.loc[i,'论文题目']))

#p3tab2.subheader('毕业生合影')
#students2020 = Image.open('photos/研究生/2020.png')
#p3tab2.image(students2020, caption='2021年太原参会')

##------------------------page3-3
p3tab3.subheader('研究生获得奖励')
grad_rewards=pd.read_csv("grad_rewards.csv")
for i in grad_rewards.index:
	p3tab3.markdown("[%d] %s, %s, %d年."%(i+1,grad_rewards.loc[i,'姓名'],grad_rewards.loc[i,'奖励名称'],grad_rewards.loc[i,'年']))


#-----------------page4
page4.subheader('本科生培养')
under_thesis=pd.read_csv("under_thesis.csv")
under_rewards=pd.read_csv("under_rewards.csv")
page4.markdown("指导本科生获各类奖项%d项，本科毕业生%d位。"%(len(under_rewards),len(under_thesis)))

p4tab1, p4tab2, p4tab3 =page4.tabs(["教授课程","指导毕业论文","指导获奖"])
##-----------------------page4-1
p4tab1.subheader('开设课程')
under_courses=pd.read_csv("under_courses.csv")
for i in under_courses.index:
	p4tab1.markdown("[%d] %s, %d学时, %d-%d学年第%d学期, 选课人数: %d人。"%(i+1,under_courses.loc[i,"课程名称"],under_courses.loc[i,"课时"],under_courses.loc[i,"学年起始"],under_courses.loc[i,"学年终止"],under_courses.loc[i,"学期"],under_courses.loc[i,"选课人数"]))

p4tab1.subheader('担任班主任')
p4tab1.markdown('2026.9-2030.6 碳中和2601班')
p4tab1.markdown('2022.9-2025.6 营销2101班')
p4tab1.markdown('2021.9-2022.9 工商2104班')
p4tab1.markdown('2019.9-2020.9 工商1908班')

##-----------------------page4-2
p4tab2.subheader('毕业论文')
for i in under_thesis.index:
	p4tab2.markdown("%d届, %s. %s."%(under_thesis.loc[i,'年'],under_thesis.loc[i,'姓名'],under_thesis.loc[i,'论文题目']))
##-----------------------page4-3
p4tab3.subheader('本科生获得奖励')

for i in under_rewards.index:
	p4tab3.markdown("[%d] %s, %s, %d年."%(i+1,under_rewards.loc[i,'姓名'],under_rewards.loc[i,'奖励名称'],under_rewards.loc[i,'年']))