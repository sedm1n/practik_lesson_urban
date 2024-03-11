# Предположим, что студент может набрать 100 % баллов на экзамене,
# получив все правильные или все неправильные ответы.
# Учитывая потенциально неполный ключ с ответами и ответы студента,
# напишите функцию, которая определяет, может ли студент набрать 100 %.
# Неполные вопросы помечаются знаком подчеркивания "_".
#
# test.assert_equals(possibly_perfect(), True)
# test.assert_equals(possibly_perfect(), True)
# test.assert_equals(possibly_perfect(, False)
#
# test.assert_equals(possibly_perfect(['B', '_'], ['C', 'A']), True)
# test.assert_equals(possibly_perfect(['B', 'A'], ['C', 'A']), False)
# test.assert_equals(possibly_perfect(['B'], ['B']), True)
#
# test.assert_equals(possibly_perfect(['_', 'T', '_', '_'], ['T', 'F', 'F', 'F']), True)
# test.assert_equals(possibly_perfect(['_', 'T', '_', '_'], ['T', 'T', 'F', 'T']), True)
# test.assert_equals(possibly_perfect(['_', 'T', 'T', 'T'], ['T', 'T', 'F', 'T']), False)
# test.assert_equals(possibly_perfect(['_', 'T', 'T', 'T'], ['T', 'T', 'T', 'T']), True)
# test.assert_equals(possibly_perfect(['_', 'T', 'T', 'T'], ['F', 'F', 'F', 'F']), True)
# test.assert_equals(possibly_perfect(['_', '_', '_', '_'], ['F', 'F', 'F', 'F']), True)

# def possibly_perfect(key, answers):
#     resul_list = []
#     if key == answers:
#         return True
#     for i, k in zip(key, answers):
#         if i == k:
#             resul_list.append(True)
#         elif i == '_' or k == '_':
#             continue
#         elif i != k:
#             resul_list.append(False)
#
#     return True if len(set(resul_list)) <= 1 else False


print(possibly_perfect(['_', '_', '_', '_'], ['M', 'F', 'F', 'F']))