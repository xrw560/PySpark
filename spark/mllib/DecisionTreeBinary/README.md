

train_data(训练数据)：以此数据训练模型
validation_data(验证数据)：作为评估模型使用
test_data(测试数据)：作为测试数据使用

1. 提取分类特征字段：
转换的方法以OneHotEncoder方式进行。如果网页分类有N个分类，就会转换为N个数值字段。处理步骤如下:
(1) 创建categories_map网页分类字典，一个分类对应一个数字
(2) 分类特征字段使用categories_map(网页分类字典)，转换为数字，例如business通过categories_map转换后categories_idx=2
(3) categories_idx=2再以OneHotEncoder方式转换为category_features_list从0算起，位置2是1，结果是0,0,1,0,0,0,0,0,0,0,0,0,0,0,共14个数值字段

2. 如何评估模型的准确率
- 使用AUC评估二元分类模型  
针对二元分类，主要是以AUC(Area under the Curve of ROC)来评估数据模型的好坏。  
tip:  
真阳性 True Positives(TP):预测为1，实际上为1  
伪阳性 False Positives(FP):预测为1，实际上为0  
真阴性 True Negatives(TN):预测为0，实际上为1  
伪阴性 False Negatives(FN):预测为0，实际上为0  
TPR:在所有实际为1的样本中被正确地判断为1的比例  
TPR=TP/(TP+FN)  
FPR:在所有实际为0的样本中被错误地判断为1的比例  
FPR=FP/(EP+TN)  
有了TPR、FPR就可以绘出ROC曲线图  
可从AUC判断二元分类的优劣  
AUC=1:最完美的情况，预测准确率100%,但是不可能存在  
0.5<AUC<1:优于随机猜测，具有预测价值  
AUC=0.5:与随机猜测一样，没有预测价值  
AUC<0.5:比随机猜测还差，但如果反向预测，就优于随机猜测  

3. 如何确认是否过度训练  
所谓过度训练(overfitting)，是指机器学学习所学到的模型过度贴近train_data，从而导致误差变得很大。为了确认没有overfitting(过度训练)问题：  
- 首先，在训练评估阶段使用validation_data评估模型
- 然后，在测试阶段使用另外一组数据test_data测试数据后再测试模型  
如果训练评估阶段时AUC很高，但是测试阶段AUC很低，就代表可能有overfitting的问题。