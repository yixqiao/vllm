from vllm import LLM

llm = LLM(
    model="gpt2-large",
    task="generate",
    tensor_parallel_size=8
)

output = llm.generate("Hello, my name is")

print(output)
