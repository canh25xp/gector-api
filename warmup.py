import sys

sys.path.append("gector")
from predict import predict, load
from huggingface_hub import hf_hub_download

roberta_path = hf_hub_download(repo_id="canh25xp/GECToR-Roberta", filename="roberta_1_gectorv2.th", cache_dir=".cache")
xlnet_path = hf_hub_download(repo_id="canh25xp/GECToR-Roberta", filename="xlnet_0_gectorv2.th", cache_dir=".cache")
bert_path = hf_hub_download(repo_id="canh25xp/GECToR-Roberta", filename="bert_0_gector.th", cache_dir=".cache")

print(f"roberta_path: {roberta_path}")
print(f"xlnet_path: {xlnet_path}")
print(f"bert_path: {bert_path}")
model_gector_roberta = load(str(roberta_path), "roberta")
model_gector_xlnet = load(str(xlnet_path), "xlnet")
model_gector_bert = load(str(bert_path), "bert")

output, cnt_corrections = predict(["He do this"], model_gector_roberta)
print(f"output model_gector_roberta: {output}", "cnt_corrections: ", cnt_corrections)
output, cnt_corrections = predict(["He do this"], model_gector_xlnet)
print(f"output model_gector_xlnet: {output}", "cnt_corrections: ", cnt_corrections)
output, cnt_corrections = predict(["He do this"], model_gector_bert)
print(f"output model_gector_bert: {output}", "cnt_corrections: ", cnt_corrections)
