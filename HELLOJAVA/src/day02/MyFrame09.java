package day02;

import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;

public class MyFrame09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame09 frame = new MyFrame09();
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
	public MyFrame09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 195, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setBounds(17, 17, 148, 26);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn1 = new JButton("1");
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				clickNum(btn1.getText());
			}
		});
		btn1.setBounds(17, 67, 58, 26);
		contentPane.add(btn1);
		
		JButton btn2 = new JButton("2");
		btn2.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				clickNum(String.valueOf(2));
			}
		});
		btn2.setBounds(72, 67, 58, 26);
		contentPane.add(btn2);
		
		JButton btn3 = new JButton("3");
		btn3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				clickNum(String.valueOf(3));
			}
		});
		btn3.setBounds(124, 67, 58, 26);
		contentPane.add(btn3);
		
		JButton btn4 = new JButton("4");
		btn4.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				clickNum(String.valueOf(4));
			}
		});
		btn4.setBounds(17, 105, 58, 26);
		contentPane.add(btn4);
		
		JButton btn5 = new JButton("5");
		btn5.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				clickNum(String.valueOf(5));
			}
		});
		btn5.setBounds(72, 105, 58, 26);
		contentPane.add(btn5);
		
		JButton btn6 = new JButton("6");
		btn6.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				clickNum(String.valueOf(6));
			}
		});
		btn6.setBounds(124, 105, 58, 26);
		contentPane.add(btn6);
		
		JButton btn7 = new JButton("7");
		btn7.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				clickNum(String.valueOf(7));
			}
		});
		btn7.setBounds(17, 144, 58, 26);
		contentPane.add(btn7);
		
		JButton btn8 = new JButton("8");
		btn8.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				clickNum(String.valueOf(8));
			}
		});
		btn8.setBounds(72, 143, 58, 26);
		contentPane.add(btn8);
		
		JButton btn9 = new JButton("9");
		btn9.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				clickNum(String.valueOf(9));
			}
		});
		btn9.setBounds(124, 144, 58, 26);
		contentPane.add(btn9);
		
		JButton btnCall = new JButton("call");
		btnCall.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String phoneNumber = tf.getText();
				JOptionPane.showMessageDialog(null,phoneNumber+"로 전화 연결중...");
			}
		});
		btnCall.setBounds(38, 205, 117, 29);
		contentPane.add(btnCall);
		
		JButton btn0 = new JButton("0");
		btn0.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				clickNum(String.valueOf(0));
			}
		});
		btn0.setBounds(72, 178, 58, 26);
		contentPane.add(btn0);
		
		JButton btnStar = new JButton("*");
		btnStar.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				clickNum("*");
			}
		});
		btnStar.setBounds(17, 177, 58, 26);
		contentPane.add(btnStar);
		
		JButton btnSharp = new JButton("#");
		btnSharp.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				clickNum("#");
			}
		});
		btnSharp.setBounds(124, 177, 58, 26);
		contentPane.add(btnSharp);
	}
	
	public void clickNum(String number){
		tf.setText(tf.getText()+number);
	}

}
