"""
Задача "Проверка на выносливость":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить класс Runner, объекты которого вам будет необходимо протестировать.

Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
    1) test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
    Далее вызовите метод walk у этого объекта 10 раз.
    После чего методом assertEqual сравните distance этого объекта со значением 50.

    2) test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
    Далее вызовите метод run у этого объекта 10 раз.
    После чего методом assertEqual сравните distance этого объекта со значением 100.

    3) test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
    Далее 10 раз у объектов вызываются методы run и walk соответственно.
    Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.

Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.

Пункты задачи:
    1) Скачайте исходный код для тестов.
    2) Создайте класс RunnerTest и соответствующие описанию методы.
    3) Запустите RunnerTest и убедитесь в правильности результатов.
"""
import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        self.alex = runner.Runner('Alex')
        for _ in range(10):
            self.alex.walk()
        self.assertEqual(self.alex.distance, 50)

    def test_run(self):
        self.oleg = runner.Runner('Oleg')
        for _ in range(10):
            self.oleg.run()
        self.assertEqual(self.oleg, 100)

    def test_challenge(self):
        self.vica = runner.Runner('Vica')
        self.marina = runner.Runner('Marina')
        for _ in range(10):
            self.vica.run()
            self.marina.walk()
        self.assertNotEqual(self.vica, self.marina)


if __name__ == '__main__':
    unittest.main()
