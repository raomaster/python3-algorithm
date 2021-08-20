from demos import bisection_iter, analyze_fun, generate_emails

list_of_domains = ['yaexample.com', 'goexample.com', 'example.com']

emails = generate_emails(10, list_of_domains, 100000)


# Append email to find
email = 'prueba@example.com'
emails.append(email)

sorted_emails = sorted(emails)

index, found = bisection_iter(email, sorted_emails)

print(found)

if index:
    print(f"element at index: {index} is {sorted_emails[index]}")
# Call functions in demo file, taking time for each random list
analyze_fun(bisection_iter, email, sorted_emails)
analyze_fun(generate_emails, 10, list_of_domains, 100000)
