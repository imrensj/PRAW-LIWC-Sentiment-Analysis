import praw


#key in the submission ID of the Reddit thread you want to scrape
sub_id = "xxxxxx"





def get_replies(comment, reply_list):

    """ recursive function that goes through the reply tree of a comment """

    reply_list.append({"id": comment.id, "comment": comment.body})

    if len(comment._replies) > 0:

        for r in comment._replies:

            get_replies(r, reply_list)

    return reply_list




#state your purpose for conducting the comment scrape
r = praw.Reddit('get comments from xxxxxxxx for xxxxxxx by User: xxxxxxxxx')

submission = r.get_submission(submission_id=sub_id)



""" this is a costly operation due to reddit's limits but is necessary

    to get all comments and prevent errors in script """

submission.replace_more_comments(limit=None, threshold=0)



# final array for writing to file

final = []



for comment in submission.comments:

    """ loops through all comments to submission """

    x = []  # array that holds the comment and all replies



    # get all replies and append it to our array for writing to file

    final.append(get_replies(comment, x))



with open('comments.csv', 'a') as outf:

    """ open file and write to it """

    # 2 dimension array needs two for loops

    for ele in final:

        for ele2 in ele:

            # write to file in the proper comma delimited format, one per line

            outf.write(u"{0},{1}\n".format(ele2['id'], ele2['comment']).encode('utf-8'))

