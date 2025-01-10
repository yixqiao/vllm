from vllm import LLM

llm = LLM(
    model="nvidia/Minitron-8B-Base",
    task="generate",
    tensor_parallel_size=8
)

output = llm.generate("Hello, my name is")

print(output)
