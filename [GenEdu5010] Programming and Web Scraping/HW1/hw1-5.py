import math

point_list_untransformed = input().split(') (')
point_1 = [int(i) for i in point_list_untransformed[0][1:].split(',')]
point_2 = [int(i) for i in point_list_untransformed[1].split(',')]
point_3 = [int(i) for i in point_list_untransformed[2].split(',')]
point_4 = [int(i) for i in point_list_untransformed[3][:-1].split(',')]
point_list = [point_1, point_2, point_3, point_4]


# barycentric method
def get_alpha_value():
    alpha_value_1 = ((point_3[1] - point_4[1]) * (point_1[0] - point_4[0]) +
                     (point_4[0] - point_3[0]) * (point_1[1] - point_4[1])) / \
                    ((point_3[1] - point_4[1]) * (point_2[0] - point_4[0]) +
                     (point_4[0] - point_3[0]) * (point_2[1] - point_4[1]))
    alpha_value_2 = ((point_4[1] - point_1[1]) * (point_2[0] - point_1[0]) +
                     (point_1[0] - point_4[0]) * (point_2[1] - point_1[1])) / \
                    ((point_4[1] - point_1[1]) * (point_3[0] - point_1[0]) +
                     (point_1[0] - point_4[0]) * (point_3[1] - point_1[1]))
    alpha_value_3 = ((point_1[1] - point_2[1]) * (point_3[0] - point_2[0]) +
                     (point_2[0] - point_1[0]) * (point_3[1] - point_2[1])) / \
                    ((point_1[1] - point_2[1]) * (point_4[0] - point_2[0]) +
                     (point_2[0] - point_1[0]) * (point_4[1] - point_2[1]))
    alpha_value_4 = ((point_2[1] - point_3[1]) * (point_4[0] - point_3[0]) +
                     (point_3[0] - point_2[0]) * (point_4[1] - point_3[1])) / \
                    ((point_2[1] - point_3[1]) * (point_1[0] - point_3[0]) +
                     (point_3[0] - point_2[0]) * (point_1[1] - point_3[1]))
    return [alpha_value_1, alpha_value_2, alpha_value_3, alpha_value_4]


def get_beta_value():
    beta_value_1 = ((point_4[1] - point_2[1]) * (point_1[0] - point_4[0]) +
                    (point_2[0] - point_4[0]) * (point_1[1] - point_4[1])) / \
                   ((point_3[1] - point_4[1]) * (point_2[0] - point_4[0]) +
                    (point_4[0] - point_3[0]) * (point_2[1] - point_4[1]))
    beta_value_2 = ((point_1[1] - point_3[1]) * (point_2[0] - point_1[0]) +
                    (point_3[0] - point_1[0]) * (point_2[1] - point_1[1])) / \
                   ((point_4[1] - point_1[1]) * (point_3[0] - point_1[0]) +
                    (point_1[0] - point_4[0]) * (point_3[1] - point_1[1]))
    beta_value_3 = ((point_2[1] - point_4[1]) * (point_3[0] - point_2[0]) +
                    (point_4[0] - point_2[0]) * (point_3[1] - point_2[1])) / \
                   ((point_1[1] - point_2[1]) * (point_4[0] - point_2[0]) +
                    (point_2[0] - point_1[0]) * (point_4[1] - point_2[1]))
    beta_value_4 = ((point_3[1] - point_1[1]) * (point_4[0] - point_3[0]) +
                    (point_1[0] - point_3[0]) * (point_4[1] - point_3[1])) / \
                   ((point_2[1] - point_3[1]) * (point_1[0] - point_3[0]) +
                    (point_3[0] - point_2[0]) * (point_1[1] - point_3[1]))
    return [beta_value_1, beta_value_2, beta_value_3, beta_value_4]


def get_gamma_value(alpha_value_list, beta_value_list):
    gamma_value_1 = 1.0 - alpha_value_list[0] - beta_value_list[0]
    gamma_value_2 = 1.0 - alpha_value_list[1] - beta_value_list[1]
    gamma_value_3 = 1.0 - alpha_value_list[2] - beta_value_list[2]
    gamma_value_4 = 1.0 - alpha_value_list[3] - beta_value_list[3]
    return [gamma_value_1, gamma_value_2, gamma_value_3, gamma_value_4]


def sorting_x_than_y(given_point_list):
    return given_point_list[0], given_point_list[1]


started_point = sorted(point_list, key=sorting_x_than_y, reverse=False)[0]
ref_vector = [0, 1]


def counterclockwise(given_point_list):
    vector = [given_point_list[0] - started_point[0], given_point_list[1] - started_point[1]]
    norm_of_vector = math.hypot(vector[0], vector[1])
    if norm_of_vector == 0:
        return -math.pi, 0
    normalized_vector = [vector[0] / norm_of_vector, vector[1] / norm_of_vector]
    dot_product = normalized_vector[0] * ref_vector[0] + normalized_vector[1] * ref_vector[1]
    diff_product = ref_vector[1] * normalized_vector[0] - ref_vector[0] * normalized_vector[1]
    angle = math.atan2(diff_product, dot_product)
    if angle < 0:
        return angle, norm_of_vector
    return -angle, norm_of_vector


try:
    alpha = get_alpha_value()
    beta = get_beta_value()
    gamma = get_gamma_value(alpha, beta)
    count = 0
    for i in range(4):
        if alpha[i] >= 0 and beta[i] >= 0 and gamma[i] >= 0:
            count += 1
    if count != 0:
        print('fail')
    else:
        sorted_counterclockwise = sorted(point_list, key=counterclockwise)
        print(sorted_counterclockwise)
except ZeroDivisionError:
    print('fail')
