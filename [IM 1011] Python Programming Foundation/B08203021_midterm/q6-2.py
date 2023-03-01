def same_or_different(txt_name_1, txt_name_2):
    with open(txt_name_1) as f1:
        with open(txt_name_2) as f2:
            if f1.read() == f2.read():
                f1.close()
                f2.close()
                return 'same'
            else:
                f1.close()
                f2.close()
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
