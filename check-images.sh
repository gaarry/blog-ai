#!/bin/bash
# 检查所有照片图片链接是否有效
cd content/photos
broken=0
for f in *.md; do
  url=$(grep "^coverImage:" "$f" | sed 's/coverImage: "\(.*\)"/\1/')
  if [ -n "$url" ]; then
    code=$(curl -s -o /dev/null -w "%{http_code}" "$url" 2>/dev/null)
    if [ "$code" != "200" ]; then
      echo "❌ $f ($code)"
      broken=$((broken + 1))
    fi
  fi
done
if [ $broken -eq 0 ]; then
  echo "✅ 所有图片链接正常"
fi
