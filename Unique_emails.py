""" Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.
Constraints:
1 <= emails.length <= 100
1 <= emails[i].length <= 100
emails[i] consist of lowercase English letters, '+', '.' and '@'.
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.
Domain names end with the ".com" suffix. """


class Solution:
    def count_unique_emails(self, emails: list) -> int:
        a = set()
        for email in emails:
            first, last = email.split('@')
            if '+' in first:
                first = first[:first.index('+')]
            a.add(first.replace('.', '') + '@' + last)
        return len(a)


emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
emails2 = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
counter = Solution()
result = counter.count_unique_emails(emails)
print(result)
