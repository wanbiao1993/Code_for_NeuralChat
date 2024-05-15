# Code_for_NeuralChat

LLM参数内含大量知识，具有一定的逻辑能力，但是想要作为机器人的控制策略还需要进一步加强。但是LLM结合思维链可以生成更加完备的逻辑。本项目将Python语言作为一种思维链的中间表达。由LLM生成这种中间表达的思维链，然后再执行这些Python文件，进而控制机械臂。通过少量示例（few-shot prompting），LLMs 能够自主地重新组合 API 调用，生成新的策略代码

本项目，仅作为复旦大学课程作业。

# 硬件要求
1. CPU: Intel(R) Xeon(R) Gold 6430 或 Intel(R) Xeon(R) Gold 6430
2. Memory:120G 以上
3. GPU:L20-48G 或 RTX 4090-24G
4. OS: Ubuntu 22.04.1 LTS

# 注意：
1. NeuralChat服务端使用Meta-Llama-3-70B-Instruct生成的Policy质量更高
2. 70B模型代码质量更高，依自己情况决定是否要量化
3. Server端的RestFul API 需要进行调整以适配OpenAI的调用接口，主要调整/v1/completions接口，调整内容，见《操作手册.pdf》
3. 对于temperature应该始终最小，这样生成的Policy代码质量更高。

参考代码：https://github.com/google-research/google-research/tree/master/code_as_policies

# 下面实验的演示视频
https://github.com/wanbiao1993/Code_for_NeuralChat/assets/131963219/95345b13-cc68-4d82-a93a-d77bf162fed3


https://github.com/wanbiao1993/Code_for_NeuralChat/assets/131963219/f87fafcf-8cff-4dd3-a753-0eb0cd6c0915



