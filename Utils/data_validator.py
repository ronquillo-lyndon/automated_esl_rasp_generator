
#code response validator
start_response = "src_ch3ck-14" # start response code
end_response = "erc_che3ck-12" # end response code

#Verify valid inputs
def _validate_input(topic_v, topic_s, nop_v, nop_s, noq_v, noq_s):
    #s = state, v = value
    topic_state = topic_s
    nop_state = nop_s
    noq_state = noq_s
    response_message = ""
    approve = False

    temp_noq = noq_v
    if temp_noq == "":
        noq_state = True
        response_message = "No number of question inputted. 2-3 paragraphs is advisable."
    else:
        try:
            temp_noq = int(temp_noq)
            if 1 <= temp_noq and 5 >= temp_noq:
                noq_state = False
            else:
                noq_state = True
                response_message = "Then number at Number Of Question should be between 1-5 only."
        except:
            noq_state = True
            response_message = "Invalid inputted value at Number Of Question. Please put a number."
    
    temp_nop = nop_v
    if temp_nop == "":
        nop_state = True
        response_message = "No number of paragraph inputted. 2-3 paragraphs is advisable."
    else:
        try:
            temp_nop = int(temp_nop)
            if 1 <= temp_nop and 5 >= temp_nop:
                nop_state = False
            else:
                nop_state = True
                response_message = "Then number at Number Of Paragraph should be between 1-5 only."
                
        except:
            nop_state = True
            response_message = "Invalid inputted value at Number Of Paragraph. Please put a number."

    if topic_v == "":
        topic_state = True
        response_message = "No topic inputted. Think something, like for example Music."
    else:
        topic_state = False        
    
    if topic_state == False and nop_state == False and noq_state == False:
        approve = True

    return {"states": 
                {"topic_state": topic_state, 
                "nop_state": nop_state, 
                "noq_state": noq_state}, 
            "approve": approve,
            "response_message": response_message}

def _validate_response(response):
    start_cut_response = response[:12]
    end_cut_response = response[-13:]
    if len(response) < 12:
        return False, "Automation Failed to Response. Try again!"
    if start_cut_response == start_response and end_cut_response == end_cut_response:
        return True, "Sucessful Response!"
    return False, "Automation Failed to Response. Try again!"

if __name__ == "__main__":
    pass