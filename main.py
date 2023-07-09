
class Stack:

    def __init__(self):
        self.current_index = -1
        self.values = []

    def is_empty(self):
        return self.current_index == -1

    def push(self, val):
        self.values.append(val)
        self.current_index += 1

    def pop(self):
        if self.is_empty():
            return 'No elements in stack'
        else:
            item = self.values.pop(self.current_index)
            self.current_index -= 1
            return item

    def peek(self):
        return self.values[self.current_index]

    def size(self):
        return len(self.values)

    def __str__(self):
        return ''.join(self.values)


if __name__ == '__main__':
    st = Stack()
    string = input('Введите последовательность скобок')
    brackets = {'(': ')', ')': '(', '{': '}', '}': '{', '[': ']', ']': '['}
    for i in string:
        if st.is_empty():
            st.push(i)
        else:
            check_item = st.pop()
            if brackets[i] != check_item:
                st.push(check_item)
                st.push(i)

    print('Сбалансировано') if st.is_empty() else print('Несбалансированно')
