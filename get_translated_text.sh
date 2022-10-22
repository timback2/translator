# Read contents from data.txt

input="keys.txt"
while IFS= read -r line
do
  echo "$line"  
  curl -H 'content-type: application/json' $es/document/_doc/_search -d '{"query":{"match":{"_id":"'$line'"}},"fields":["title","text"],"_source":false}' | jq >> translated/"$line"_translated.json

done < "$input"
