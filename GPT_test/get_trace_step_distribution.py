import change_point
import step_rt


if __name__ == '__main__':
    change_point.main("/Users/joytsai/Desktop/JoyTsai/Lab/Data/20220916_s2_1-4-836bp-220nm-0.5xRRM/",
                          "/Users/joytsai/Desktop/JoyTsai/Lab/Data/20220916_s2_1-4-836bp-220nm-0.5xRRM/2022-09-20-895Srr--fitresults_reshape_analyzed.xlsx",
                          dead_time_start=48.65895, dead_time_end=114.5628, end_time=None)
    step_rt.main("/Users/joytsai/Desktop/JoyTsai/Lab/Data/20220916_s2_1-4-836bp-220nm-0.5xRRM/",
                     BM_min=70, BM_max=130)
