import filecmp  ##python內建模組，但我還是有附上filecmp.py，畢竟課上沒提到過我就附上了。


def same_or_different(txt_name_1, txt_name_2):
    if filecmp.cmp(txt_name_1, txt_name_2):
        return 'same'
    else:
        return 'different'


print(f"m6-1-1.txt and m6-1-2.txt => {same_or_different('m6-1-1.txt', 'm6-1-2.txt')}")
print(f"m6-1-1.txt and m6-2-1.txt => {same_or_different('m6-1-1.txt', 'm6-2-1.txt')}")
print(f"m6-1-1.txt and m6-2-2.txt => {same_or_different('m6-1-1.txt', 'm6-2-2.txt')}")
print(f"m6-1-1.txt and m6-3-1.txt => {same_or_different('m6-1-1.txt', 'm6-3-1.txt')}")
print(f"m6-1-1.txt and m6-3-2.txt => {same_or_different('m6-1-1.txt', 'm6-3-2.txt')}")
print(f"m6-1-2.txt and m6-2-1.txt => {same_or_different('m6-1-2.txt', 'm6-2-1.txt')}")
print(f"m6-1-2.txt and m6-2-2.txt => {same_or_different('m6-1-2.txt', 'm6-2-2.txt')}")
print(f"m6-1-2.txt and m6-3-1.txt => {same_or_different('m6-1-2.txt', 'm6-3-1.txt')}")
print(f"m6-1-2.txt and m6-3-2.txt => {same_or_different('m6-1-2.txt', 'm6-3-2.txt')}")
print(f"m6-2-1.txt and m6-2-2.txt => {same_or_different('m6-2-1.txt', 'm6-2-2.txt')}")
print(f"m6-2-1.txt and m6-3-1.txt => {same_or_different('m6-2-1.txt', 'm6-3-1.txt')}")
print(f"m6-2-1.txt and m6-3-2.txt => {same_or_different('m6-2-1.txt', 'm6-3-2.txt')}")
print(f"m6-2-2.txt and m6-3-1.txt => {same_or_different('m6-2-2.txt', 'm6-3-1.txt')}")
print(f"m6-2-2.txt and m6-3-2.txt => {same_or_different('m6-2-2.txt', 'm6-3-2.txt')}")
print(f"m6-3-1.txt and m6-3-2.txt => {same_or_different('m6-3-1.txt', 'm6-3-2.txt')}")
