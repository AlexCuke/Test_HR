class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Проверка стека на пустоту."""
        return len(self.items) == 0

    def push(self, item):
        """Добавляет новый элемент на вершину стека."""
        self.items.append(item)

    def pop(self):
        """Удаляет верхний элемент стека и возвращает его."""
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """Возвращает верхний элемент стека, не удаляя его."""
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        """Возвращает количество элементов в стеке."""
        return len(self.items)


def check_balance(sequence):
    stack = Stack()
    # Словарь соответствия закрывающей скобки открывающей
    brackets_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for char in sequence:
        # Если скобка открывающая — кладем в стек
        if char in brackets_map.values():
            stack.push(char)
        # Если скобка закрывающая
        elif char in brackets_map.keys():
            # Если стек пуст или верхушка стека не совпадает с парой — дисбаланс
            if stack.is_empty() or stack.pop() != brackets_map[char]:
                return "Несбалансированно"
    
    # В конце стек должен быть пустым
    if stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"

# Тестирование
if __name__ == "__main__":
    balanced_list = [
        "(((([{}]))))",
        "[([])((([[[]]])))]{()}",
        "{{[()]}}"
    ]
    
    unbalanced_list = [
        "}{}",
        "{{[(])]}}",
        "[[{())}]"
    ]

    print("-- Положительные тесты --")
    for seq in balanced_list:
        print(f"{seq}: {check_balance(seq)}")

    print("\n-- Отрицательные тесты --")
    for seq in unbalanced_list:
        print(f"{seq}: {check_balance(seq)}")