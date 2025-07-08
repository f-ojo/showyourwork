from fast_dash import FastDash

def simple_text_to_text(input_text: str) -> str:
    return input_text

app = FastDash(simple_text_to_text)

if __name__ == '__main__':
    app.run()