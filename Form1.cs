using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace 计算器
{
    public partial class Form1 : Form
    {
        TextBox display;
        double firstNumber = 0;
        string operatorSymbol = "";
        bool isOperatorClicked = false;

        public Form1()
        {
            InitializeComponent();
            InitializeCalculator();
        }

        private void InitializeCalculator()
        {
            this.Text = "简单计算器";
            this.Size = new Size(300, 400);

            display = new TextBox();
            display.ReadOnly = true;
            display.TextAlign = HorizontalAlignment.Right;
            display.Font = new Font("Arial", 20);
            display.Dock = DockStyle.Top;
            display.Height = 50;
            this.Controls.Add(display);

            string[] buttons = {
                "7","8","9","/",
                "4","5","6","*",
                "1","2","3","-",
                "C","0","=","+"
            };

            int top = 60;
            int left = 10;
            int width = 60;
            int height = 50;

            for (int i = 0; i < buttons.Length; i++)
            {
                Button btn = new Button();
                btn.Text = buttons[i];
                btn.Size = new Size(width, height);
                btn.Left = left;
                btn.Top = top;

                btn.Font = new Font("Arial", 14);

                if (char.IsDigit(btn.Text[0]))
                    btn.Click += Number_Click;
                else if (btn.Text == "C")
                    btn.Click += Clear_Click;
                else if (btn.Text == "=")
                    btn.Click += Equal_Click;
                else
                    btn.Click += Operator_Click;

                this.Controls.Add(btn);

                left += width + 5;

                if ((i + 1) % 4 == 0)
                {
                    left = 10;
                    top += height + 5;
                }
            }
        }

        private void Number_Click(object sender, EventArgs e)
        {
            Button btn = sender as Button;

            if (isOperatorClicked)
            {
                display.Text = "";
                isOperatorClicked = false;
            }

            display.Text += btn.Text;
        }

        private void Operator_Click(object sender, EventArgs e)
        {
            Button btn = sender as Button;

            if (display.Text == "") return;

            firstNumber = Convert.ToDouble(display.Text);
            operatorSymbol = btn.Text;
            isOperatorClicked = true;
        }

        private void Equal_Click(object sender, EventArgs e)
        {
            if (display.Text == "") return;

            double secondNumber = Convert.ToDouble(display.Text);
            double result = 0;

            switch (operatorSymbol)
            {
                case "+":
                    result = firstNumber + secondNumber;
                    break;
                case "-":
                    result = firstNumber - secondNumber;
                    break;
                case "*":
                    result = firstNumber * secondNumber;
                    break;
                case "/":
                    if (secondNumber != 0)
                        result = firstNumber / secondNumber;
                    else
                    {
                        MessageBox.Show("不能除以0");
                        return;
                    }
                    break;
            }

            display.Text = result.ToString();
        }

        private void Clear_Click(object sender, EventArgs e)
        {
            display.Text = "";
            firstNumber = 0;
            operatorSymbol = "";
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}