import shutil
import os

def ipr_copy(cross_info, cross_name, dataset):
    test = 0
    val = 1
    train = 2
    dst_path = '../../cross/'

    for in_folder in cross_info[test]:
        in_folder_path = '../' + dataset + '/' + in_folder
        dst_folder_path = dst_path + cross_name + '/test/' + in_folder
        shutil.copytree(in_folder_path,dst_folder_path)
    for in_folder in cross_info[val]:
        in_folder_path = '../' + dataset + '/' + in_folder
        dst_folder_path = dst_path + cross_name + '/val/' + in_folder
        shutil.copytree(in_folder_path,dst_folder_path)
    for in_folder in cross_info[train]:
        in_folder_path = '../' + dataset + '/' + in_folder
        dst_folder_path = dst_path + cross_name + '/train/' + in_folder
        shutil.copytree(in_folder_path,dst_folder_path)
    
# test val train の順
cross1 = [['0'],['3_1', '3_2'],['1_1', '1_2', '1_3', '22', '23', '24', '25', '26', '27', '28', '29', '30', '4_1', '4_2', '5', '6_1', '6_2', '6_3']]
cross2 = [['1_2','1_3','23','24','6_3'],['0'],['1_1','3_1','25','26','27','28','29','30','3_2','4_1','4_2','5','6_1','6_2','22']]
cross3 = [['29','6_1','1_1'],['0'],['1_2','1_3','22','23','24','25','26','27','28','30','3_1','3_2','4_1','4_2','5','6_2','6_3']]
con_cross1 = [['con_0'],['con_3_1', 'con_3_2'],['con_1_1', 'con_1_2', 'con_1_3', 'con_22', 'con_23', 'con_24', 'con_25', 'con_26', 'con_27', 'con_28', 'con_29', 'con_30', 'con_4_1', 'con_4_2', 'con_5', 'con_6_1', 'con_6_2', 'con_6_3']]
con_cross2 = [['con_1_2','con_1_3','con_23','con_24','con_6_3'],['con_0'],['con_1_1','con_3_1','con_25','con_26','con_27','con_28','con_29','con_30','con_3_2','con_4_1','con_4_2','con_5','con_6_1','con_6_2','con_22']]
con_cross3 = [['con_29','con_6_1','con_1_1'],['con_0'],['con_1_2','con_1_3','con_22','con_23','con_24','con_25','con_26','con_27','con_28','con_30','con_3_1','con_3_2','con_4_1','con_4_2','con_5','con_6_2','con_6_3']]
synthetic5662_cross1 = [['0'],['3_1','3_2'],['1_1','1_2','1_3','22','23','24','25','26','27','28','29','30','4','5','6_1','6_2','6_3']]
synthetic5662_cross2 = [['1_2','1_3','23','24','6_3'],['0'],['1_1','22','25','26','27','28','29','30','3_1','3_2','4','5','6_1','6_2']]
synthetic5662_cross3 = [['29','6_1','1_1'],['0'],['1_2','1_3','22','23','24','25','26','27','28','30','3_1','3_2','4','5','6_2','6_3']]
# ipr_copy(cross1, 'cross1', 'test')
# ipr_copy(cross1, 'cross1', 'val')
# ipr_copy(cross1, 'cross1', 'train')
#ipr_copy(cross2, 'cross2', 'test')
#ipr_copy(cross2, 'cross2', 'val')
#ipr_copy(cross2, 'cross2', 'train')
# ipr_copy(cross3, 'cross3', 'test')
# ipr_copy(cross3, 'cross3', 'val')
# ipr_copy(cross3, 'cross3', 'train')

# ipr_copy(con_cross1, 'con_cross1', 'test')
# ipr_copy(con_cross1, 'con_cross1', 'val')
# ipr_copy(con_cross1, 'con_cross1', 'train')
# ipr_copy(con_cross2, 'con_cross2', 'test')
# ipr_copy(con_cross2, 'con_cross2', 'val')
# ipr_copy(con_cross2, 'con_cross2', 'train')
# ipr_copy(con_cross3, 'con_cross3', 'test')
# ipr_copy(con_cross3, 'con_cross3', 'val')
# ipr_copy(con_cross3, 'con_cross3', 'train')

# ipr_copy(synthetic5662_cross1, 'synthetic5662_cross1','synthetic5662')
# ipr_copy(synthetic5662_cross2, 'synthetic5662_cross2','synthetic5662')
ipr_copy(synthetic5662_cross3, 'synthetic5662_cross3','synthetic5662')

