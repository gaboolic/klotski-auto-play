本项目可以用来识别屏幕图片，自动完成新仙剑奇侠传二里的拼图(数字华容道)小游戏

klotski/klotski99可用来对9x9大小的数字华容道求解，可能是全网唯一一份9x9大小的数字华容道求解python代码

python版本3.10，tensorflow==2.15.0

用uiautomator2控制安卓手机截屏

使用opencv处理图片 灰度 二值化 提取图片序号

使用tensorflow训了个卷积神经网络识别数字

使用dfs搜索拼图移动路径(9x9大小的数字华容道使用A*算法按顺序逐步拼好，先拼n-2层然后拼最后两层，7秒左右耗时，感觉一层层拼可能速度会更快)

最后再把路径转为屏幕坐标 用uiautomator2控制安卓手机点击

99%的代码是引到chatgpt完成再拼凑

安卓控制用https://github.com/openatx/uiautomator2

9x9数字华容道解法参考https://github.com/dkl520/Digital-Huarong-Road

项目路径：

- gameimg 存储游戏图片用于训练
- klotski 数字华容道解法
- recognition 使用tensorflow训练、识别数字，有2个模型，一个用来判断是否数字，一个用来识别数字，后来想了想其实用一个网络就行，把num_classes从10改成11就行
- template 存储分割后的数字模板用于训练

main.py为主文件

dealnumber.py用来测试图片分割，test.py用来测试图片识别+华容道解法