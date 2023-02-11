#!/usr/bin/env python
# coding: utf-8

import re
import time
import random

"""
nd - k = 100
n - k = 1
n(d-1) = 99 = 3 x 3 x 11
k = n - 1

n = 3, d = 34, k = 2
n = 9, d = 12, k = 8
n = 11, d = 10, k = 10
n = 33, d = 4, k = 32
"""


class DiceApp:

    def __init__(self):
        self.command = ""
        self.result = []

    def throw_dice(self, command):
        self.command = command
        self.result = []
        dice_list = re.findall(r"\d+d\d+", command)
        random.seed(time.time())
        for dice in dice_list:
            num, size = [int(x) for x in dice.split("d")]
            dice_result = [random.randint(1, size) for x in range(num)]
            self.result.append(dice_result)
    
    def show_result(self):
        command_items = re.split(r"(\d+d\d+)", self.command)
        processed_items = []
        for item in command_items:
            if re.match(r"\d+d\d+", item):
                dice_result = self.result.pop(0)
                processed_items.append(f"sum({str(dice_result)})")
            else:
                processed_items.append(item)
        expr = "".join(processed_items)
        print(f"{self.command} = {expr} = {eval(expr)}")


if __name__ == "__main__":
    d = DiceApp()
    while True:
        print("-"*20)
        dice_command = input("请输入dice指令:\n")
        if dice_command in ["q", "quit", "exit"]:
            exit()
        elif re.search(r"\d+d\d+", dice_command):
            d.throw_dice(dice_command)
            d.show_result()
        else:
            print("指令有误，请重试！")
