import pickle
from batchgenerators.utilities.file_and_folder_operations import subfiles, save_pickle, load_pickle

# p = open(r'E:\AutoSeg_Bladder_data\nnUnet\nnUNet_trained_models\nnUNet\3d_cascade_fullres\Task501_bladder\nnUNetTrainerV2CascadeFullRes__nnUNetPlansv2.1\plans.pkl', 'rb')
# p = open(r'E:\AutoSeg_Bladder_data\nnUnet\nnUNet_preprocessed\Task501_bladder\nnUNetPlansv2.1_plans_3D.pkl', 'rb')
# p = open(r'E:\AutoSeg_Bladder_data\nnUnet\nnUNet_preprocessed\Task504_ctvfull\dataset_properties.pkl', 'rb')
plan_pkl = r'/media/lu/Data/Data/nnUnet/nnUNet_preprocessed/Task502_rectum/nnUNetPlansv2.1_plans_3D.pkl'
data = load_pickle(plan_pkl)
data['preprocessed_data_folder'] = '/media/lu/Data/Data/nnUnet/nnUNet_preprocessed/Task502_rectum'
cropped_data_dir = r'/media/lu/Data/Data/nnUnet/nnUNet_raw_data_base/nnUNet_cropped_data/Task502_rectum'
# for x in range(len(data['list_of_npz_files'])):
#     data['list_of_npz_files'][x] = cropped_data_dir + '/' + data['list_of_npz_files'][x].split("\\")[-1]
#     # split = data['list_of_npz_files'][x].split("/")
# save_pickle(data, plan_pkl)
# twod_plan_pkl = r'/media/lu/Data/Data/nnUnet/nnUNet_preprocessed/Task502_rectum/nnUNetPlansv2.1_plans_2D.pkl'
# twod_plan = load_pickle(twod_plan_pkl)
# print(twod_plan)

plans_pkl = r'/media/lu/Data/Data/nnUnet/nnUNet_trained_models/nnUNet/3d_lowres/Task502_rectum/nnUNetTrainerV2__nnUNetPlansv2.1/plans.pkl'
plan_data = load_pickle(plans_pkl)
# plan_data['preprocessed_data_folder'] = '/media/lu/Data/Data/nnUnet/nnUNet_preprocessed/Task502_rectum'
# for x in range(len(plan_data['list_of_npz_files'])):
#     plan_data['list_of_npz_files'][x] = cropped_data_dir + '/' + plan_data['list_of_npz_files'][x].split("\\")[-1]
#     # split = plan_data['list_of_npz_files'][x].split("/")
#     print()
# save_pickle(plan_data, plans_pkl)
# print()

#
# for x in range(len(data['list_of_npz_files'])):
#     # data['list_of_npz_files'][x] = cropped_data_dir + '/' + data['list_of_npz_files'][x].split("\\")[-1]
#     # split = data['list_of_npz_files'][x].split("/")
#     print()
# # save_pickle(data, plan_pkl)
# print(data)
#
pkl_files = subfiles(r'/media/lu/Data/Data/nnUnet/nnUNet_preprocessed/Task502_rectum/nnUNetData_plans_v2.1_stage0', suffix='.pkl')
labelsTrBase = r'/media/lu/Data/Data/nnUnet/nnUNet_raw_data_base/nnUNet_raw_data/Task502_rectum/labelsTr'
imagesTrBase = r'/media/lu/Data/Data/nnUnet/nnUNet_raw_data_base/nnUNet_raw_data/Task502_rectum/imagesTr'
for pkl in pkl_files:
    # p = open(pkl, 'r+b')
    data_pkl = load_pickle(pkl)
    # seg_file = data_pkl['seg_file'].split('\\')[-1]
    # data_pkl['seg_file'] = labelsTrBase + '/' + seg_file
    # data_file = data_pkl['list_of_data_files'][0].split('\\')[-1]
    # data_pkl['list_of_data_files'][0] = imagesTrBase + '/' + data_file
    # save_pickle(data_pkl, pkl)
    print()
