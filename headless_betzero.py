from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

# Telegram bot details
TELEGRAM_BOT_TOKEN = "7859722593:AAGJrtKuWjWOaXMP94b7QmKFAD52GkhAo7k"
TELEGRAM_CHAT_ID =  '1916073059'

def send_telegram_message(message):
    """Send a message to the Telegram bot."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to send Telegram message: {e}")


def repeat():
    # Configure Firefox Options
    firefox_options = Options()
    firefox_options.add_argument("--headless")  # Run in headless mode

    # Start WebDriver using GeckoDriverManager
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=firefox_options)

    # Open Target Webpage
    driver.get("https://logigames.bet9ja.com/Games/Launcher?gameId=11000&provider=0&pff=1&skin=201")

    print("=" * 50)
    print("WELCOME TO ALL-STARS TECH")
    print("=" * 50)

    driver.implicitly_wait(5)

    while True:
        try:
            wait = WebDriverWait(driver, 5)

            # Get game time
            game_time_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='timeline__value-txt']")))
            game_time = int(game_time_element.text)

            if game_time >= 38:
                print(f"Game Time: {game_time} - Fetching Data...")

                # Open stats
                try:
                    stat = driver.find_element(By.XPATH, "//div[@class='stats']/div")
                    stat.click()
                    sleep(2)
                except Exception as e:
                    print("Error: Could not open stats.", str(e))

                # Extract row 1 numbers
                row1 = []
                for i in range(1, 7):
                    try:
                        row1.append(int(driver.find_element(By.XPATH, f"//table/tbody/tr[1]/td[2]/div/span[{i}]").text))
                    except:
                        row1.append(None)  

                print("row1:", row1)

      
                # Click necessary elements
                try:
                    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div[4]/div[1]/div[7]/a").click()
                    sleep(1)
                    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div[4]/div[1]/div[7]/div/div[1]/div").click()
                    sleep(1)
                except Exception as e:
                    print("Error clicking stats elements:", str(e))

                # Extract btotals dynamically
                btotals = []
                for i in range(1, 50):
                    try:
                        element = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[{i}]/td[2]")
                        btotals.append(int(element.text) if element.text.isdigit() else 0)
                    except:
                        btotals.append(0)

                print("btotals 100:", btotals)

                # Extract max values and adjust dynamically
                max_s_values = []
                for i in range(1, 50):
                    try:
                        element = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[{i}]/td[5]")
                        max_s_values.append(int(element.text) if element.text.isdigit() else 1)
                    except:
                        max_s_values.append(1)

                print("max_s_values100:", max_s_values)

                #######################################
                  # Click necessary elements
                try:
                    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div[4]/div[1]/div[7]/a").click()
                    sleep(1)
                    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div[4]/div[1]/div[7]/div/div[2]/div").click()
                    sleep(1)
                except Exception as e:
                    print("Error clicking stats elements:", str(e))

                # Extract btotals dynamically
                btotals24 = []
                for i in range(1, 50):
                    try:
                        element = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[{i}]/td[2]")
                        btotals24.append(int(element.text) if element.text.isdigit() else 0)
                    except:
                        btotals24.append(0)

                print("btotals24:", btotals24)

                # Extract max values and adjust dynamically
                max_s_values24 = []
                for i in range(1, 50):
                    try:
                        element = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div/main/div[4]/div[2]/table/tbody/tr[{i}]/td[5]")
                        max_s_values24.append( int(element.text) if element.text.isdigit() else 100)
                    except:
                        max_s_values24.append(100)

                print("max_s_values24:", max_s_values24)





                streak100_m9 = sorted(enumerate(max_s_values, start=1), key=lambda x: x[1], reverse=True)[-9:]
                streak24_m9 = sorted(enumerate(max_s_values24, start=1), key=lambda x: x[1], reverse=True)[-9:]
            

                    # Extract indices of the top 9 numbers
                low_streak24 = [index for index, _ in streak24_m9]
                low_streak100 = [index for index, _ in streak100_m9]
                
                #print(" 9 highest max streak :", max_streak)
                print("lowest streak 24hr :", low_streak24)
                print("")
                #print(" 9 highest max streak :", max_streak)
                print("lowest streak 100 :", low_streak100)
                print("")
                com_streak = list(set(low_streak24) & set(low_streak100))
                print("common streak", com_streak)
                print("")


                                    # Sort numbers in descending order while keeping track of indices
                #streak100_+9 = sorted(enumerate(all_bmax_streak1, start=1), key=lambda x: x[1], reverse=True)[:9]
                total100_9 = sorted(enumerate(btotals, start=1), key=lambda x: x[1], reverse=True)[:9]
                total24_9 = sorted(enumerate(btotals24, start=1), key=lambda x: x[1], reverse=True)[:9]
            

                    # Extract indices of the top 9 numbers
                high_t24 = [index for index, _ in total24_9]
                high_t100 = [index for index, _ in total100_9]
                
                #print(" 9 highest max streak :", max_streak)
                print("highest 24hr :", high_t24)
                print("")
                #print(" 9 highest max streak :", max_streak)
                print("highest 100 :", high_t100)
                print("")
                com_high = list(set(high_t24) & set(high_t100))
                print("common streak", com_high)
                print("")

                print("==" * 20)
                com_com1 = list(set(low_streak100) & set(high_t100))
                com_com2 = list(set(low_streak24) & set(high_t24))
                print("common high and streak100", com_com1)
                print("")
                print("common high and streak24", com_com2)
                print("")
                message = (f"100 draws are {com_com1}--- 24hrs draws are {com_com2}\n")
                      
                send_telegram_message(message)

        except TimeoutException:
            print("Timeout occurred, retrying...")
            continue
        except StaleElementReferenceException:
            print("Stale element, refreshing page...")
            driver.refresh()
            sleep(3)
            continue
        except Exception as e:
            print("Unexpected error:", str(e))
            break

    driver.quit()
