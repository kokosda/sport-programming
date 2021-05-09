"""
Input
The input to the function/method consists of five arguments -
numFeatures, an integer representing the number of possible features;
topFeatures, an integer representing the number of top features that your function returns (N);
possibleFeatures, a list of sigle-word strings representing the possible features;
numFeatureRequests, an integer representing the number of feature requests;
featureRequests, a list of strings where each element is a string that consists of space-separeted words representing feature requests.
"""
from typing import List

class Solution:
    def get_top_features(
        self,
        numFeatures: int, 
        topFeatures: int,
        possibleFeatures: List[str],
        numFeatureRequests: int, 
        featureRequests: List[str]
    ) -> List[str]:
        possible_features_sorted = sorted(possibleFeatures)
        possible_features_map = { k:0 for k in possible_features_sorted }

        for i in range(numFeatureRequests):
            words_set = set(featureRequests[i].lower().split())

            for w in words_set:
                if possible_features_map.get(w) is not None:
                    possible_features_map[w] -= 1
        
        possible_features_sorted.sort(key=lambda x: possible_features_map[x])
        res = possible_features_sorted[:topFeatures]
        return res

num_features = 6
top_features = 2
possible_features = ["storage", "battery", "hover", "alexa", "waterproof", "solar"]
num_feature_requests = 7
feature_requests = [
    "I wish my Kindle had even more storage", 
    "I wish the battery life on my Kindle lasted 2 years", 
    "I read in the bath and would enjoy a waterproof Kindle",
    "I want to take my Kindle into the hover.",
    "Waterproof please waterproof!", 
    "It would be neat if my Kindle would hover on my desk when not in use",
    "How cool would it be if my Kindle charged in the sun via solar power?"
]

solution = Solution()

res = solution.get_top_features(num_features, top_features, possible_features, num_feature_requests, feature_requests)

print(res)

"""
Example
Input:
numFeatures = 6
topFeatures = 2
possibleFeatures = ["storage", "battery", "hover", "alexa", "waterproof", "solar"]
numFeatureRequests = 7
featureRequests = ["I wish my Kindle had even more storage",
"I wish the battery life on my Kindle lasted 2 years", "I read in the bath and would enjoy a waterproof Kindle",
"I want to take my Kindle into the hover. Waterproof please waterproof!", "It would be neat if my Kindle would hover on my desk when not in use",
"How cool would it be if my Kindle charged in the sun via solar power?"]

Output
["waterproof", "battery"]

Explanation:
"waterproof" occurs in three different requests and "battery" in two. "hover", "solar", and "storage" occur in only one request each.
"""