import preprocess as pre
import eval 
import json

def find_text(text,target):
    pre.stopwordslist("./bin/stopwords.txt")

    nn = eval.simChCheck()
    max_sim = 0
    res  = " "
    for value in text.values():
        result = nn.forward(value,target)
        result_dict = json.loads(result)

        # 现在可以提取 similarity 的值了
        similarity = result_dict["similarity"]
        if similarity > max_sim:
            max_sim = similarity
            res = value
    print(res)

if __name__ == "__main__":
    text = {
        "text1" : "这句话呢，其实都是告诉你游戏规则，他就看你能不能看到他这个给你的规定了。",
        "text2" : "或者说你骂人一个游戏，它上面会有一个游戏的一个，这个攻略对不对？",
    }
    target = "这段话其实是告诉你游戏规则，你要好好看，好好理解他的规定。"
    find_text(text,target)

