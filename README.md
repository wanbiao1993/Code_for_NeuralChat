# Code_for_NeuralChat


LLM参数内含大量知识，具有一定的逻辑能力，但是想要作为机器人的控制策略还需要进一步加强。但是LLM结合思维链可以生成更加完备的逻辑。本项目将Python语言作为一种思维链的中间表达。由LLM生成这种中间表达的思维链，然后再执行这些Python文件，进而控制机械臂。

LLM生成Python代码是关键，需要精心设计其提示工程，例如变量命名和结构化的程序生成。

本项目，仅作为复旦大学课程作业。

下一步：
1. 使用更小的LLM后端，由机械臂自身的Edge设备运行
2. 放入DOFBOT机械臂中


# 注意：
1. NeuralChat服务端使用Phind/Phind-CodeLlama-34B-v2生成的Policy质量更高
2. 70B模型代码质量更高，依自己情况决定是否要量化
3. Server端的RestFul API 需要进行调整以适配OpenAI的调用接口，主要调整/v1/completions接口
3. 对于temperature应该始终最小，这样生成的Policy代码质量更高。

参考代码：https://github.com/google-research/google-research/tree/master/code_as_policies

# 下面是仿真实验的演示视频
https://github.com/wanbiao1993/Code_for_NeuralChat/assets/131963219/95345b13-cc68-4d82-a93a-d77bf162fed3

<!-- mp4格式 -->
<video id="video" controls="" preload="none" poster="封面">
      <source id="mp4" src="__temp__.mp4" type="video/mp4">
</videos>

