
    account_a = get_random_account(data)
    account_b = get_random_account(data)

    while game_should_continue:
        while account_a == account_b:
                account_b = get_random_account()

        print(f"score: {score}")
        print("Compare A: " + account_a["name"] + " a " + account_a["description"] + " from " +  account_a["country"])
        print(vs)
        print("Against B: " + account_b["name"] + " a " + account_b["description"] + " from " +  account_b["country"])

        guess = input("A or B: ").lower()
        if compare(account_a["follower_count"], account_b["follower_count"] ,guess):
            score += 1