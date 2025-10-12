from collections import deque

suggested_links = deque(int(x) for x in input().split())  # FIFO
featured_articles = [int(x) for x in input().split()]  # LIFO
target_eng_value = int(input())
final_feed_collection = []

# use modulo operation (%)

while suggested_links and featured_articles:
    first_link = suggested_links.popleft()
    first_article = featured_articles.pop()

    if first_article > first_link:
        remainder = first_article % first_link
        final_feed_collection.append(remainder)
        if remainder == 0:
            continue
        featured_articles.append(2 * remainder)

    elif first_link > first_article:
        remainder = first_link % first_article
        final_feed_collection.append(-abs(remainder))
        if remainder == 0:
            continue
        suggested_links.append(2 * remainder)

    elif first_link == first_article:
        final_feed_collection.append(0)

total_engagement_value = sum(final_feed_collection)

final_message = ""
if total_engagement_value >= target_eng_value:
    # success
    final_message = f"Goal achieved! Engagement Value: {total_engagement_value}"
else:
    # fail
    shortfall = target_eng_value - total_engagement_value
    final_message = f"Goal not achieved! Short by: {shortfall}"

print("Final Feed: " + ", ".join([str(x) for x in final_feed_collection]))
print(final_message)