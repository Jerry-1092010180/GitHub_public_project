using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace 变色窗体
{
    public partial class Form1 : Form
    {
        private bool isRed = false;
        public Form1()
        {
            InitializeComponent();
        }

        private void 按钮_Click(object sender, EventArgs e)
        {
            if (!isRed)
            {
                this.BackColor = Color.Red;
                isRed = true;
            }
            else
            {
                this.BackColor = Color.Blue;
                isRed = false;
            }
        }
    }
}
