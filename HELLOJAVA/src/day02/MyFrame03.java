package day02;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.JTextField;

/*
 * 숙제 : MyFrame02 만들고, Jlabel 넣고 (lbl) 숫자넣고 버튼 Jbtn(btn) 만들고, 클릭하면 라벨에 써있는 숫자가 계속 증가하게끔 구현하기. 
 */

public class MyFrame03 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_a;
	private JTextField tf_b;
	private JTextField tf_3;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame03 frame = new MyFrame03();
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
	public MyFrame03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf_a = new JTextField();
		tf_a.setBounds(21, 115, 72, 26);
		contentPane.add(tf_a);
		tf_a.setColumns(10);
		
		JLabel lblNewLabel = new JLabel("+");
		lblNewLabel.setBounds(105, 120, 61, 16);
		contentPane.add(lblNewLabel);
		
		tf_b = new JTextField();
		tf_b.setBounds(137, 115, 72, 26);
		contentPane.add(tf_b);
		tf_b.setColumns(10);
		
		JButton btnNewButton = new JButton("=");
		btnNewButton.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int numA = Integer.parseInt(tf_a.getText());
				int numB = Integer.parseInt(tf_b.getText());
				tf_3.setText(String.valueOf(numA+numB));
			}
		});
		btnNewButton.setBounds(221, 116, 55, 26);
		contentPane.add(btnNewButton);
		
		tf_3 = new JTextField();
		tf_3.setBounds(288, 115, 93, 26);
		contentPane.add(tf_3);
		tf_3.setColumns(10);
	}
}
