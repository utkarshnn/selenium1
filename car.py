from selenium import webdriver
browser = webdriver.Firefox()
home_page = "https://stage.raptorsupplies.com/"

def check_page_broken_links(self, url):
# Sample usage:
#     check_page_broken_links(self,"https://stage.raptorsupplies.com/") 
#         will return empty list if all links in the page work fine
#         else it will return list of all the broken links 
#                                    (either link text, or link href)
#   Will check for -  i) "Page Not found" error
#                     ii) Redirects

    try:
        failed = []
        self.implicitly_wait(5)
        self.get(url)
        number_of_links = len(self.find_elements_by_tag_name('a'))

        for i in range(number_of_links):
            # Save current browser window handle
            initial_window = self.current_window_handle 
            ## print "initial_window_handle:      ", initial_window

            link = self.find_elements_by_tag_name('a')[i]
            link_address = link.get_attribute("href")
            link_name = link.text
            print "link checked: ",i,": ",link_name,": ",link_address

            if ((link_address is not None) 
                and ("google" not in link_address) 
                and ("mailto" not in link_address) 
                and is_link_element_displayed(self,element=link) is True):
                  link.click() # link clicked
                  open_windows = self.window_handles
                  ## print "window_handles:      ", open_windows

                  # Navigate to the browser window where 
                  #               latest page was opened
                  self.switch_to_window(open_windows[-1])
                  ## print "current_window_handle:"
                  ## print self.current_window_handle
                  time.sleep(5)
                  print "defined: ",link_address
                  print "current: ", self.current_url

                  if (link_address[-1] == "#" 
                       and self.current_url in 
                        [link_address, link_address[:-1],
                                      link_address[:-2],link_address+'/']):
                          # A "#" at the end means user 
                          # will stay on the same page.(Valid scenario) 
                          pass  
                  elif (self.current_url not in 
                        [link_address,
                         home_page + link_address[1:]]): 
                        # if user lands up in a page different 
                        #                    from that intended 
                        if link_name:
                          failed.append(link_name)
                        else:
                          failed.append(link_address)

                  if len(self.window_handles) > 1:  
                          # close newly opened window
                          self.close()

                  # Switch to main browser window
                  self.switch_to_window(open_windows[0]) 

            self.get(url)
    except Exception, e: 
           return ['Exception occurred while checking',e]
    return failed

# call defined function to check broken links in carwale.com home page
print check_page_broken_links(browser,"https://stage.raptorsupplies.com/")
