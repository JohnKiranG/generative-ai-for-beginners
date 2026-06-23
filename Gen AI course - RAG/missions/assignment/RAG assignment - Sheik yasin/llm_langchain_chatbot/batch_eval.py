# batch_eval.py

import json
from rag_chain import build_rag_chain

with open("questions.json") as f:
    questions = json.load(f)["questions"]

print("\n===== Batch Evaluation =====\n")

for idx, q in enumerate(questions, 1):
    rag = build_rag_chain()
    result = rag(q)

    print(f"Q{idx}: {q}")
    print(f"A{idx}: {result['answer']}")
    print(f"Source PDF: {result['source']}")
    print("-" * 60)

print("\n✅ Batch evaluation complete!\n")