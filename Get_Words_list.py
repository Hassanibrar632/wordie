import gradio as gr

def get_words(filename):
    with open(filename, 'r') as file:
        words = file.readlines()
    words = [word.strip().replace('"', '') for word in words]
    words = [word for word in words if len(word) == 5]
    return words

class wordie:
    def __init__(self):
        self.setofwords = words

    def view_words(self):
        return self.setofwords

    def remove_letter(self, letters):
        for letter in letters.lower():
            self.setofwords = [i for i in self.setofwords if letter not in i]
        return

    def found_letter(self, letters):
        for letter in letters.lower():
            self.setofwords = [i for i in self.setofwords if letter in i]
        return
    
    def fix_pos(self, pair):
        for letter, index in pair:
            self.setofwords = [i for i in self.setofwords if letter == i[index]]
        return

    def reset(self):
        self.setofwords = words
        return

def process_input(l1, l2, l3, l4, l5, yellow, black):
    gusser.reset()

    word = [l1, l2, l3, l4, l5]
    pair = []
    for i, l in enumerate(word):
        try:
            int(l)
        except:
            pair.append([l.lower(), i])
    gusser.fix_pos(pair)
    
    gusser.found_letter(yellow)
    gusser.remove_letter(black)
    
    return "\n".join(gusser.view_words())

words = get_words(r'wordlist-20210729.txt')
gusser = wordie()

# Building the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("### Enter the letter at the correct position: ")
    with gr.Row():
      l1 = gr.Textbox(label="t1", value="1", max_lines=1)
      l2 = gr.Textbox(label="t2", value="2", max_lines=1)
      l3 = gr.Textbox(label="t3", value="3", max_lines=1)
      l4 = gr.Textbox(label="t4", value="4", max_lines=1)
      l5 = gr.Textbox(label="t5", value="5", max_lines=1)

    with gr.Row():
      yellow_input = gr.Textbox(label="Yellow", value="")
      black_input = gr.Textbox(label="Black", value="")

    with gr.Row():
        output_box = gr.Textbox(label="Output", placeholder="Processed output will be shown here", interactive=False)
        process_button = gr.Button("Process")

    # Link the process button to the processing function
    process_button.click(
        fn=process_input, 
        inputs=[l1, l2, l3, l4, l5, yellow_input, black_input], 
        outputs=[output_box]
    )

demo.launch()