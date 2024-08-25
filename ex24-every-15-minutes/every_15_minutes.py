def print_times() -> None:
    hh = 12
    mm = 0
    mer = 'am'
    
    while str(hh) + str(mm) + str(mer) != '1145pm':
        print(f'{hh}:{mm:02} {mer}')
        if mm < 45:
            mm += 15
            continue
        else:
            if hh == 11:
                if mer == 'am':
                        mer = 'pm'
                elif mer == 'pm':
                    mer = 'am'
            if hh < 12:
                hh += 1
                mm = 0
                continue
            if hh == 12:
                hh = 1
                mm = 0
                continue
    print(f'{hh}:{mm:02} {mer}')
