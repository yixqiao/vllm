from vllm import LLM

llm = LLM(
    model="Qwen/Qwen2-7B",
    task="generate",
    tensor_parallel_size=8
)

output = llm.generate("Hello, my name is")

print(output)
