#Sharv Utpat
#CS 4375.HON
#Vincent Ng
#9/10/23

import math
import sys
import node


def compute_accuracy_by_size(training_data,labels, test_data):
    curr_size = 0
    curr_training_data = []
    for i in range(8):
        for j in range(100):
            curr_training_data.append(training_data[curr_size + j])
        curr_size += 100
        root = create_tree(curr_training_data, labels)
        accuracy = compute_accuracy(root, test_data, labels, len(test_data))
        #print(f"currsize = {curr_size} accuracy = {accuracy}", )

def main():
    #print(sys.argv)
    training_data_file = sys.argv[1]
    test_data_file = sys.argv[2]
    #print(training_data_file)
    training_data, labels = parse_train(training_data_file)
    test_data, labels2 = parse_train(test_data_file)
    training_size = len(training_data)
    test_size = len(test_data)
    root = create_tree(training_data, labels)
    #print("main: printing tree")
    node.dfs(root)
    data_size = len(training_data)
    accuracy1 = "{:.1f}".format(compute_accuracy(root,training_data,labels,data_size))
    print('')
    print('Accuracy on training set (', training_size, ' instances): ' ,accuracy1, '%', sep='' )
    print('')
    #compute_accuracy(root,training_data,labels)
    data_size = len(test_data)
    accuracy2 = "{:.1f}".format(compute_accuracy(root,test_data,labels2,data_size))
    print('Accuracy on test set (', test_size, ' instances): ', accuracy2, '%', sep='')
    #compute_accuracy(root,test_data, labels2)
    compute_accuracy_by_size(training_data,labels, test_data)

def get_label_value(row,label,labels):
    label_index = -1
    for curr_label in labels:
        label_index = label_index + 1
        if (label == curr_label):
            break
    return row[label_index]

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def get_outcome(root,row,labels):
    trav = root
    while trav is not None:
        if is_number(trav.data):
            return trav.data
        label = trav.data
        label_value = get_label_value(row,label,labels)
        if label_value == 0:
            trav = trav.left;
        else:
            if label_value == 1 :
                trav = trav.middle
            elif label_value == 2 :
                trav = trav.right
    print("")

def compute_accuracy(root,data,labels, data_size):
    column_count = len(data[0])
    error_count = 0
    for row in data:
        outcome = get_outcome(root,row,labels)
        if (outcome != row[column_count-1]):
            error_count +=1
    accuracy = 100*(data_size - error_count)/data_size
    return accuracy
    #print(f"{accuracy}")

def get_max_key_variance(training_data, number_of_features):
    for i in range(number_of_features):
        column = get_column(training_data,i)
        if not is_outcome_column_unique(column):
            return i
    return 0

def step_function(training_data, labels):
    num_columns = len(labels)
    regular_columns = num_columns - 1

    # print(labels)
    grand_column_number = len(labels) - 1
    column = get_column(training_data, grand_column_number)
    map = get_frequency(column)

    higher_entropy = calculate_higher_entropy(map)
    #print(f"step_function : higher_entropy = {higher_entropy}")

    list_IGs = []

    for i in range(regular_columns):
        #print("step_function : Column Number:", i)
        #print('step_function : Label: ', labels[i])
        column_number = i
        column = get_column(training_data, column_number)
        #print(f"step_function : column = {column}")
        map = get_frequency(column)
        #print(f"step_function : map = {map}")
        map = dict(sorted(map.items()))
        #print("step_function : Distribution:", map)
        matrix = (get_distribution_matrix(training_data, column_number, grand_column_number))
        list_entropies = calculate_entropy(matrix)
        #print(f"step_function : list_entropies = {list_entropies}")
        list_weights = compute_weights(map)
        #print(f"step_function : list_weights = {list_weights}")
        information_gain = compute_IG(higher_entropy, list_entropies, list_weights)
        list_IGs.append(information_gain)
        #print("step_function : Information gain:", information_gain)
        #print('')

    #print(list_IGs)
    best_feature, column_number = get_most_informative_feature(list_IGs, labels,training_data)
    #print("Best feature is", best_feature)
    return best_feature, column_number

def filter_dataset(training_data, column_number, column_value):
    filtered_dataset = []
    for i in range(len(training_data)):
        row = training_data[i]
        if row[column_number] == column_value:
            filtered_dataset.append(row)

    return filtered_dataset

def get_high_freeq_value(array):
    map={}
    for element in array:
        if map.get(element) is None:
            map[element] = 1
        else:
            map[element] = map[element]+1
    max_freeq = 0
    high_freeq_key = 0
    for key in map:
        if map[key] > max_freeq:
            max_freeq = map[key]
            high_freeq_key = key
    return high_freeq_key

def is_outcome_column_unique(array):
    element = array[0]
    for i in range(1,len(array)):
        if (element != array[i]):
            return False
    return True

def create_tree(training_data, labels):
    #print(f"create_tree : training_date.len = {len(training_data)}")
    output_column_number = len(labels) - 1
    output_column = get_column(training_data, output_column_number)

    if len(training_data) == 1 or is_outcome_column_unique(output_column):
        return node.Node(training_data[0][output_column_number])
    best_feature, column_number = step_function(training_data, labels)
    #print(f"create_tree : best_feature = {best_feature}, column_number = {column_number}")
    root = node.Node(best_feature)
    subset0 = filter_dataset(training_data, column_number, 0)
    subset1 = filter_dataset(training_data, column_number, 1)
    subset2 = filter_dataset(training_data, column_number, 2)

    if len(subset0) == len(training_data):
        output_column = get_column(training_data,output_column_number)
        high_freeq_value = get_high_freeq_value(output_column)
        return node.Node(high_freeq_value)
    else:
        if len(subset0) == 0:
            root.left = node.Node(0)
            root.left_label = 0
        if 0 < len(subset0) <= len(training_data):
            child0 = create_tree(subset0, labels)
            root.left = child0
            root.left_label = 0

    if len(subset1) == len(training_data):
        output_column = get_column(training_data, output_column_number)
        high_freeq_value = get_high_freeq_value(output_column)
        return node.Node(high_freeq_value)
    else:
        if len(subset1) == 0:
            root.middle = node.Node(0)
            root.middle_label = 1
        if 0 < len(subset1) <= len(training_data):
            child1 = create_tree(subset1, labels)
            root.middle = child1
            root.middle_label = 1

    if len(subset2) == len(training_data):
        output_colum = get_column(training_data, output_column_number)
        high_freeq_value = get_high_freeq_value(output_colum)
        return node.Node(high_freeq_value)
    else:
        if len(subset2) == 0:
            root.right = node.Node(0)
            root.right_label = 2
        if 0 < len(subset2) <= len(training_data):
            child2 = create_tree(subset2, labels)
            root.right = child2
            root.right_label = 2
    return root



def get_most_informative_feature(list_IGs, labels,training_data):
    highest_information_gain = max(list_IGs)
    if (highest_information_gain == 0):
        max_index = get_max_key_variance(training_data,len(labels)-1)
    else:
        max_index = list_IGs.index(highest_information_gain)
    return labels[max_index], max_index


def compute_weights(map):
    #print(f"compute_weights : map = {map}")
    list = map.values()
    sum1 = sum(list)
    weights = []
    for items in list:
        items /= sum1
        weights.append(items)
    return weights

def compute_IG(higher_entropy, list_entropies, list_weights):
    #print(f"compute_IG : entropies.length = {len(list_entropies)}, weights.length = {len(list_weights)}")
    information_gain = higher_entropy
    length = len(list_weights)
    for i in range(length):
        #print(f"i= {i}")
        information_gain -= list_entropies[i] * list_weights[i]
    return information_gain

def parse_train(filename):
    #print(f"Processing file {filename}")
    line_number = 0
    array=[]
    with open(filename, 'r') as f:
        for line in f:
            #print(line)
            if line_number == 0:
                #print(f"ignoring row line - {line}")
                header = line
                labels = header.split()
                line_number += 1
                # skip row line
            else:
                # parse line
                row = line.split()
                int_list = [int(i) for i in row]
                #print(f"parsing row line - {int_list}")
                array.append(int_list)

    #print(array)
    return array, labels

def get_column(array, column_number):
    class_column = []
    for row in array:
        class_column.append(row[column_number])
    return class_column

def get_frequency(column):
    map = {0: 0, 1: 0, 2: 0}
    for i in column:
        freq = map.get(i)
        map[i] = freq + 1
        #print(freq)
    #print(map)
    return map

def calculate_higher_entropy(map):
    list = map.values()
    sum = 0
    for i in list:
        sum += i
    #print(sum)
    entropy = 0
    for i in list:
        if i != 0:
            entropy += (-1 * (i/sum) * math.log(i/sum, 2))
        else:
            entropy += 0
    #print(entropy)
    return(entropy)

def get_distribution_matrix(array, column_number, grand_column_number):
    matrix = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    for row in array:
        dist_row = row[column_number]
        dist_col = row[grand_column_number]
        matrix[dist_row][dist_col] += 1
    return matrix

def calculate_entropy(matrix):
    row_sum = 0
    list_entropies = []
    entropy = 0

    for rows in matrix:
        row_sum = sum(rows)
        for items in rows:
            if items != 0:
                entropy += (-1 * (items / row_sum) * math.log(items / row_sum, 2))

            else:
                entropy += 0
        list_entropies.append(entropy)
        entropy = 0


    return list_entropies


main()
