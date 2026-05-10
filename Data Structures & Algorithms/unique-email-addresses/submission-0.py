class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:

            local, domain = email.split("@")

            cleaned = ""

            for ch in local:

                if ch == '+':
                    break

                if ch != '.':
                    cleaned += ch

            final_email = cleaned + "@" + domain

            unique.add(final_email)

        return len(unique)