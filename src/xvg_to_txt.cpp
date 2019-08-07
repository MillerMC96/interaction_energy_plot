#include <iostream>
#include <fstream>
#include <string>

int main(int argc, char* argv[])
{
    std::ifstream input_xvg;
    std::ofstream output_txt;
    std::string line;

    input_xvg.open(argv[1]);
    output_txt.open(argv[2]);

    while (std::getline(input_xvg, line)) {
        if (line[0] == '@' || line[0] == '#') {
            continue;
        } else {
            output_txt << line << std::endl;
        }
    }

    input_xvg.close();
    output_txt.close();
}
