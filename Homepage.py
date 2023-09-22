import streamlit as st
import pandas as pd
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
st.sidebar.markdown("诚招勤奋、好学、踏实的研究生, 急需有编程背景的同学。待遇从优！")
st.sidebar.markdown("E-mail: wangge@ncepu.edu.cn")
st.sidebar.markdown("地址: 北京市昌平区北农路2号")
st.sidebar.map(pd.DataFrame(pd.Series([40.088243727163956,116.30600799534605],index=['lat', 'lon']),columns=['Ncepu']).T)

col1,col2=st.columns([9,1])
col1.subheader("王歌 博士")
col1.markdown("**华北电力大学 经济与管理学院 讲师, 硕士生导师**")

myphoto = Image.open('photos/homepage.jpeg')
col2.image(myphoto)


page1, page2, page3, page4 =st.tabs(["个人简历","科研工作","研究生培养","本科生培养"])

#-----------------page1
page1.subheader("个人简历")

page1.markdown("2019 至今 华北电力大学 经济与管理学院 讲师")

p1tab1, p1tab2, p1tab3 =page1.tabs(["教育经历","研究兴趣","招生需求"])
#tab1.markdown('**工作和教育经历**')

p1tab1.markdown("[1] 2014-2019 中国石油大学（北京）中国能源战略研究院/经济管理学院 硕博连读")
p1tab1.markdown("[2] 2018-2019 美国加州大学伯克利分校 劳伦斯伯克利国家实验室 联合培养")
p1tab1.markdown("[3] 2009-2013 南京大学 天文与空间科学学院 本科")


#tab2.markdown('**研究兴趣**')

p1tab2.markdown("- 电氢交通耦合系统")
p1tab2.markdown("- 可再生能源经济与政策")
p1tab2.markdown("- 复杂网络与博弈")

#tab3.markdown('**招生方向**')

p1tab3.markdown("- 具有经济学、能源、环境、计算机相关背景")
p1tab3.markdown("- 对能源环境经济和管理具有兴趣")
p1tab3.markdown("- 具备英文论文阅读能力")

#-----------------page2
page2.subheader("科研工作")

papers=pd.read_csv("publications.csv")
projects=pd.read_csv("projects.csv")
rewards=pd.read_csv("rewards.csv")

page2.markdown("- 累计发表论文%d篇"%len(papers))
page2.markdown("- 主持科研项目%d项, 累计承担经费:  %.1f万元"%(len(projects[projects["参与情况"]=="主持"]),projects["金额"].sum()))
page2.markdown("- 获得各类奖项%d项"%len(rewards))

p2tab1, p2tab2, p2tab3 =page2.tabs(["发表论文","承担项目","获得奖项"])

item=0
year=papers.iloc[0].loc["Year"]
p2tab1.markdown("**%d**"%year)
for i in papers.index:
	if papers.loc[i,'Year']<year:
		year=papers.loc[i,'Year']
		p2tab1.markdown("**%d**"%year)
	p2tab1.markdown("[%d] %s"%(item+1,papers.loc[i,'papers']))
	item+=1

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

#-----------------page3

page3.subheader('研究生培养')

grad_thesis=pd.read_csv("grad_thesis.csv")

page3.markdown("组内有在读全日制硕士研究生13人，非全日制硕士研究生10人，已毕业硕士研究生%d人。"%(len(grad_thesis)))

p3tab1, p3tab2, p3tab3 =page3.tabs(["在读同学","指导毕业论文","指导获奖"])

##------------------------page3-1
majors=["工业工程与管理","物流工程与管理","工商管理"]

p3tab1.subheader('在读-2023级')

p3tab1.markdown('(%s 全日制) **马嘉蔚, 栾则宇, 郭晓文.**'%majors[0])
p3tab1.markdown('(%s 全日制) **卢子仪, 卢天翼.**'%majors[2])
p3tab1.markdown('(%s 非全日制) **张豆豆, 杨田田, 杨学伟.**'%majors[2])
p3tab1.text('\n')

p3tab1.subheader('在读-2022级')

p3tab1.markdown('(%s 全日制) **程煜, 谭宇璇.**'%majors[0])
p3tab1.markdown('(%s 非全日制) **康晓杰, 古明越, 赵铭路, 李梓熙, 周舟.**'%majors[0])
p3tab1.markdown('(%s 全日制) **尹亭, 冯楚怡.**'%majors[1])
p3tab1.text('\n')

p3tab1.subheader('在读-2021级')
p3tab1.markdown('(%s 全日制) **张禾.**'%majors[0])
p3tab1.markdown('(%s 非全日制) **郑越.**'%majors[0])
p3tab1.markdown('(%s 全日制) **李智, 毛瑀璇, 钱嘉琪.**'%majors[1])
#students2021 = Image.open('photos/研究生/2021.png')
#p3tab1.image(students2021, caption='2022年初聚餐')
#p3tab1.text('\n')

p3tab1.subheader('在读-2020级')
p3tab1.markdown('(%s 非全日制) **纪金杉.**'%majors[0])

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
p4tab1.markdown('2022.9 至今 营销2101班')
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