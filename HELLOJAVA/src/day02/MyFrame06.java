package day02;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyFrame06 extends JFrame {

	private JPanel contentPane;
	private JTextField input;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame06 frame = new MyFrame06();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MyFrame06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 243, 294);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JTextArea ta = new JTextArea();
		ta.setBounds(19, 17, 107, 214);
		contentPane.add(ta);
		
		input = new JTextField();
		input.setText("2");
		input.setBounds(142, 37, 47, 29);
		contentPane.add(input);
		input.setColumns(10);
		
		JButton btn = new JButton("출력");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int inputNum = Integer.parseInt(input.getText());
				String result = inputNum + "단의 구구단 결과\n";
				result += inputNum + " * " + "1 = " + inputNum*1 + "\n";
				result += inputNum + " * " + "2 = " + inputNum*2 + "\n";
				result += inputNum + " * " + "3 = " + inputNum*3 + "\n";
				result += inputNum + " * " + "4 = " + inputNum*4 + "\n";
				result += inputNum + " * " + "5 = " + inputNum*5 + "\n";
				result += inputNum + " * " + "6 = " + inputNum*6 + "\n";
				result += inputNum + " * " + "7 = " + inputNum*7 + "\n";
				result += inputNum + " * " + "8 = " + inputNum*8 + "\n";
				result += inputNum + " * " + "9 = " + inputNum*9 + "\n";
				ta.setText(result);
			}
		});
		btn.setBounds(133, 78, 75, 29);
		contentPane.add(btn);
	}

}
