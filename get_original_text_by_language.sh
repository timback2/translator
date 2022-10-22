# Read contents from data.txt

input="languages.txt"
while IFS= read -r line
do
  echo "$line"
  curl -H 'content-type: application/json' $es/translated-document/_search -d '{"size":20, "query": { "bool":{"must" : { "term" : {"language":"'$line'"}}}}}' | jq >> output/"$line"_esresults.json
done < "$input"
